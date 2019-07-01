from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
# install neopixel library: sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
import board
import neopixel
import time
from random import randint
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy as np
import pickle


""" 
Class to initialize and display Neopixels as battery status indicator and data status indicator in the background to prevent freezing of GUI
[+] +batt_status_led()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class status_led(QThread):
    digital_pin = board.D18 # the pin number that Neopixel is connected to Pi
    num_pixels = 2    # number of Neopixels in a strip 
    brightness = 0.5  # brightness of Neopixel LEDs
    led_off = True    # flag to turn on or off the LEDs

    # parameters for battery status
    battery_good = (0,255,0)    #green for good
    batt_good_thres = 70
    battery_weak = (255,211,0)  #yellow for weak
    battery_critic = (255,0,0)    #red for critical
    batt_critic_thres = 30 
    batt_status = 1
    #pyqtSignal to store battery value of this thread to be emitted during running
    batt_data_updated = pyqtSignal(list, name='batt_updated')
    
    # parameters for data status
    data_good = (0,0,255)    #blue for good
    no_data = (0,0,0)    #none for no data
    data_status = 1
    #pyqtSignal to store data transmission status of this thread to be emitted during running
    data_updated = pyqtSignal(str, name='data_updated')

    def __init__(self):
        QThread.__init__(self)
        self.pixels = neopixel.NeoPixel(self.digital_pin, self.num_pixels, brightness=self.brightness)
        self.batt_data_thread = batt_data_status()
        self.batt_data_thread.start()

    def __del__(self):
        print("Stopping thread status_led")
        self.wait()


    def run(self):
        while not self.led_off:
            self.batt_status = self.batt_data_thread.batt_status
            self.data_status = self.batt_data_thread.data_status
            self.batt_status_label = "{:.1f}%".format(self.batt_status)
            if self.batt_status > self.batt_good_thres:
                self.pixels[0] = self.battery_good
            elif self.batt_status < self.batt_critic_thres:
                self.pixels[0] = self.battery_critic
            else:
                self.pixels[0] = self.battery_weak
            if self.data_status == 1:
                self.pixels[1] = self.data_good
                self.data_status_label = "OK"
            elif self.data_status == 0:
                self.pixels[1] = self.no_data
                self.data_status_label = "OFF"
            self.pixels.show()
            self.batt_data_updated.emit([str(self.batt_status_label), self.data_status_label])
        self.pixels.fill((0,0,0))
        self.pixels.show()

""" 
Class to check for battery status in the background to prevent freezing of GUI
[+] +batt_status()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

with open("soc_curves.pkl", "rb") as fh:
    soc_crvs = pickle.load(fh)
availableCs = np.array([0.2, 0.5, 1.0, 2.0])

def get_lo(dischargeRate):
    """
    Get the lower available curve
    """
    return np.max(availableCs[availableCs < dischargeRate])

def get_hi(dischargeRate):
    """
    Get the higher available curve
    """
    return np.min(availableCs[availableCs > dischargeRate])

def get_soc(dischargeRate, voltage):
    """
    Takes in the momentary discharge rate (in C) and the voltage.
    Returns the current state of charge (SOC) in percents (0-100)
    Interpolates based on the 4 available curves (0.2C, 0.5C, 1C, 2C).
    Anything beyond the range gets clipped to 0.2C-2C.
    """
    dischargeRate = float(dischargeRate)
    dischargeRate = np.clip(dischargeRate,min(availableCs),max(availableCs))
    if dischargeRate in availableCs:
        voltage = np.clip(voltage, np.nanmin(soc_crvs["v_{:.1f}C".format(dischargeRate)]), np.nanmax(soc_crvs["v_{:.1f}C".format(dischargeRate)]))
        soc = 100 - np.interp(voltage,
                         soc_crvs["v_{:.1f}C".format(dischargeRate)][np.logical_not(np.isnan(soc_crvs["v_{:.1f}C".format(dischargeRate)]))],
                         soc_crvs["soc_{:.1f}C".format(dischargeRate)][np.logical_not(np.isnan(soc_crvs["soc_{:.1f}C".format(dischargeRate)]))])
        return np.clip(soc, 0, 100)
    else:
        rate_hi = get_hi(dischargeRate)
        v_hi = np.clip(voltage, np.nanmin(soc_crvs["v_{:.1f}C".format(rate_hi)]), np.nanmax(soc_crvs["v_{:.1f}C".format(rate_hi)]))
        soc_hi =  100 - np.interp(v_hi,
                            soc_crvs["v_{:.1f}C".format(rate_hi)][np.logical_not(np.isnan(soc_crvs["v_{:.1f}C".format(rate_hi)]))],
                            soc_crvs["soc_{:.1f}C".format(rate_hi)][np.logical_not(np.isnan(soc_crvs["soc_{:.1f}C".format(rate_hi)]))])
        
        rate_lo = get_lo(dischargeRate)
        v_lo = np.clip(voltage, np.nanmin(soc_crvs["v_{:.1f}C".format(rate_lo)]), np.nanmax(soc_crvs["v_{:.1f}C".format(rate_lo)]))
        soc_lo =  100 - np.interp(v_lo,
                            soc_crvs["v_{:.1f}C".format(rate_lo)][np.logical_not(np.isnan(soc_crvs["v_{:.1f}C".format(rate_lo)]))],
                            soc_crvs["soc_{:.1f}C".format(rate_lo)][np.logical_not(np.isnan(soc_crvs["soc_{:.1f}C".format(rate_lo)]))])
        #print(soc_lo, soc_hi, rate_lo, rate_hi)
        return np.clip(soc_lo + (dischargeRate - rate_lo) * (soc_hi - soc_lo) / (rate_hi - rate_lo), 0, 100)


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)

class batt_data_status(QThread):
    batt_status = 1
    data_status = 1

    def __init__(self):
        QThread.__init__(self)   

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            #TODO: ask for battery status here
            # as example, generating random integers between -1, 0, 1
            #self.batt_status = randint(-1, 1)
            vBat = chan0.voltage * 2
            iBatRaw = chan1.voltage * 2
            vHighHalf = chan2.voltage
            iBat = (iBatRaw - vHighHalf) / 0.185
            cDis = iBat / 6.6
            soc = get_soc(cDis, vBat)
            print("{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}\t{:>5.3f}".format(vBat, iBatRaw, vHighHalf, iBat, cDis, soc))
            self.batt_status = soc*100

            # print(self.batt_status)
            #TODO: ask for data status here
            # for now generating random integers between  0, 1
            self.data_status = randint(0, 1)
           
            time.sleep(5.0)




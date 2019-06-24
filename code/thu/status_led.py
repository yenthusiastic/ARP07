from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
# install neopixel library: sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
import board
import neopixel
import time
from random import randint


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
    battery_weak = (255,211,0)  #yellow for weak
    battery_critic = (255,0,0)    #red for critical
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
            if self.batt_status == 1:
                self.pixels[0] = self.battery_good
                self.batt_status_label = "GOOD"
            elif self.batt_status == 0:
                self.pixels[0] = self.battery_weak
                self.batt_status_label = "LOW"
            elif self.batt_status == -1:
                self.pixels[0] = self.battery_critic
                self.batt_status_label = "CRITICAL"
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
            # for now generating random integers between -1, 0, 1
            self.batt_status = randint(-1, 1)
            # print(self.batt_status)
            #TODO: ask for data status here
            # for now generating random integers between  0, 1
            self.data_status = randint(0, 1)
           
            time.sleep(5.0)




from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
# install neopixel library: sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
import board
import neopixel
import time
from random import randint


""" 
Class to initialize and display 1st Neopixel as battery status indicator in the background to prevent freezing of GUI
[+] +batt_status_led()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class batt_status_led(QThread):
    digital_pin = board.D18 # the pin number that Neopixel is connected to Pi
    num_pixels = 1    # number of Neopixels in a strip (if applicable)
    brightness = 0.5
    battery_good = (0,255,0)    #green for good
    battery_weak = (255,211,0)  #yellow for weak
    battery_critic = (255,0,0)    #red for critical
    led_off = True
    batt_status = 1

    def __init__(self):
        QThread.__init__(self)
        self.pixels = neopixel.NeoPixel(self.digital_pin, self.num_pixels, brightness=self.brightness)
        self.get_batt_thread = batt_status()
        self.get_batt_thread.start()

    def __del__(self):
        print("Stopping thread batt_status_led")
        self.wait()


    def run(self):
        while not self.led_off:
            self.batt_status = self.get_batt_thread.batt_status
            if self.batt_status == 1:
                self.pixels.fill(self.battery_good)
            elif self.batt_status == 0:
                self.pixels.fill(self.battery_weak)
            elif self.batt_status == -1:
                self.pixels.fill(self.battery_critic)
            self.pixels.show()
        self.pixels.fill((0,0,0))
        self.pixels.show()

""" 
Class to check for battery status in the background to prevent freezing of GUI
[+] +batt_status()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class batt_status(QThread):
    batt_status = 1

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
            time.sleep(3.0)


""" 
Class to initialize and display 2nd Neopixel as data status indicator in the background to prevent freezing of GUI
[+] +data_status_led()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""
class data_status_led(QThread):
    digital_pin = board.D23 # the pin number that Neopixel is connected to Pi
    num_pixels = 1    # number of Neopixels in a strip (if applicable)
    brightness = 0.5
    data_good = (0,0,255)    #blue for good
    no_data = (0,0,0)    #none for no data
    led_off = True
    data_status = 1

    def __init__(self):
        QThread.__init__(self)
        self.pixels = neopixel.NeoPixel(self.digital_pin, self.num_pixels, brightness=self.brightness)
        #TODO init get data thread
        #self.get_data_thread = data_status()
        #self.get_data_thread.start()

    def __del__(self):
        print("Stopping thread data_status_led")
        self.wait()


    def run(self):
        while not self.led_off:
            #TODO get data status
            #self.data_status = 
            if self.data_status == 1:
                self.pixels.fill(self.data_good)
            elif self.batt_status == 0:
                self.pixels.fill(self.no_data)
            self.pixels.show()
        self.pixels.fill((0,0,0))
        self.pixels.show()


            
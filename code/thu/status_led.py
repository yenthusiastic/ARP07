from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
# install neopixel library: sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
import board
import neopixel


""" 
Class to initialize and display Neopixel as status indicator in the background to prevent freezing of GUI
[+] +status_led()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class status_led(QThread):
    digital_pin = board.D18 # the pin number that Neopixel is connected to Pi
    num_pixels = 1    # number of Neopixels in a strip (if applicable)
    brightness = 0.5
    battery_good = (0,255,0)    #green for good
    battery_weak = (255,211,0)  #yellow for weak
    battery_critic = (255,0,0)    #red for critical
    
    def __init__(self):
        QThread.__init__(self)
        self.pixels = neopixel.NeoPixel(digital_pin, num_pixels, brightness=brightness)


    def __del__(self):
        self.wait()

    def run(self, batt_status):
        while True:
            if batt_status == 1:
                self.pixels.fill(self.battery_good)
            elif batt_status == 0:
                self.pixels.fill(self.battery_weak)
            elif batt_status == -1:
                self.pixels.fill(self.battery_critic)
            else: self.pixels.fill(self.battery_weak)
            self.pixels.show()


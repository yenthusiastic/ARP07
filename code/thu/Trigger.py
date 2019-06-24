from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
# install neopixel library: sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
import board
from gpiozero import Button
import time



""" 
Class to initialize and read trigger button in the background to prevent freezing of GUI
[X] +detect_button_trigger(): integer --> trigger_reader(): class
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""
class trigger_reader(QThread):
    trigger_pin = 13 # the pin number that the trigger is connected to Pi
    btn = Button(trigger_pin)  #set this pin as pulled up
    #pyqtSignal to store time data of this thread to be emitted during running
    trigger_updated = pyqtSignal(bool, name='trigger_updated')
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        print("Stopping thread trigger reaader")
        self.wait()


    def run(self):
        while True:
            if self.btn.is_pressed:
                self.trigger_updated.emit(True)
            time.sleep(0.5)

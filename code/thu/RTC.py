from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import sys
import time
import datetime
from libs.SDL_DS3231 import SDL_DS3231


""" 
Class to retrieve RTC real time in the background to prevent freezing of GUI
[X] +RTC()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class RTC(QThread):
    default_I2C_addr = 0x68
    time_updated = pyqtSignal(str, name='time_updated')
    def __init__(self):
        QThread.__init__(self)
        self.ds3231 = SDL_DS3231(1, self.default_I2C_addr)
        self.ds3231.write_now()
        

    def __del__(self):
        print("Stopping thread RTC")
        self.wait()

    def run(self):
        while True:
            time_str = str(self.ds3231.read_datetime()).split(".")[0]
            #print('RTC time: %s' % time_str)
            self.time_updated.emit(str(time_str))
            time.sleep(1.0)

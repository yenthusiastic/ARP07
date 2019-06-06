from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import sys
import time
import datetime
#import SDL_DS3231 

class get_RTC(QThread):
    time_updated = pyqtSignal(str, name='time_updated')
    def __init__(self):
        QThread.__init__(self)
        self.ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
        self.ds3231.write_now()
        

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            time_str = str(self.ds3231.read_datetime()).split(".")[0]
            #print('RTC time: %s' % time_str)
            self.time_updated.emit(str(time_str))
            time.sleep(1.0)

        
    
class get_Rpi_time(QThread):
    time_updated = pyqtSignal(str, name='time_updated')
    def __init__(self):
        QThread.__init__(self)
        

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            time_str = str(datetime.datetime.utcnow()).split(".")[0]
            #print('RPi time: %s' % time_str)
            self.time_updated.emit(str(time_str))
            time.sleep(1.0)
    
from PyQt5.QtCore import QThread
import sys
import time
import datetime
import SDL_DS3231 

class get_RTC(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.ds3231 = SDL_DS3231.SDL_DS3231(1, 0x68)
        self.ds3231.write_now()

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            print('Raspberry Pi time: ' + time.strftime('%Y-%m-%d %H:%M:%S'))
            print('RTC time: %s' % self.ds3231.read_datetime())

            time.sleep(10.0)
        
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import sys
import time
import datetime


""" 
Classes to handle tasks that should be done in the background to prevent freezing of GUI
Thread classes to be implements, as defined in Software Architecture:
[X] +RTC() --> get_RTC()
[X] +GPS() --> get_GPS()
[+] +get_PC_time()  #show time from PC in dev environment as RTC is not possible

NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""


class get_PC_time(QThread):
    time_updated = pyqtSignal(str, name='time_updated')
    def __init__(self):
        QThread.__init__(self)
        

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            time_str = str(datetime.datetime.utcnow()).split(".")[0]
            #print('PC time: %s' % time_str)
            self.time_updated.emit(str(time_str))
            time.sleep(1.0)

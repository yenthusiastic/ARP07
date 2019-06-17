from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import sys
import time
from libs.mtk3999 import mt3339


""" 
Class to retrieve GPS data in the background to prevent freezing of GUI
[.] +GPS()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class GPS(QThread):
    default_serial_port = "/dev/tty/ACM0" #example default serial port
    #pyqtSignal to store GPS data of this thread to be emitted during running
    gps_updated = pyqtSignal(str, name='gps_updated')
    def __init__(self):
        QThread.__init__(self)
        self.gps = mt3339(self.default_serial_port)
        # TODO: check mtk3999.py for example commands to initialize gps

    def __del__(self):
        print("Stopping thread GPS")
        self.wait()

    def run(self):
        while True:
            # using dummy data for now
            # TODO: add function to read correct GPS data
            gps_str = "51.2345, 60.9876" 

            # emit GPS data to the GUI thread that is calling this thread
            self.gps_updated.emit(str(gps_str))
            time.sleep(1.0)
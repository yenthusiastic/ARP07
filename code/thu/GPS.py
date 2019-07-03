from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import sys
import time
import serial #sudo apt-get install python3-serial
import libs.adafruit_gps as adafruit_gps


""" 
Class to retrieve GPS data in the background to prevent freezing of GUI
[.] +GPS()
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""
DEFAULT_SERIAL_PORT = "/dev/ttyS0" #example default serial port
DEFAULT_BAUD_RATE = 9600 #example default baud rate

class GPS(QThread):
    #pyqtSignal to store GPS data of this thread to be emitted during running
    gps_updated = pyqtSignal(str, name='gps_updated')
    gps_str = None
    def __init__(self):
        QThread.__init__(self)
        #initialize GPS module
        self.uart = serial.Serial(port = DEFAULT_SERIAL_PORT, baudrate = DEFAULT_BAUD_RATE, timeout = 3.0)
        self.gps = adafruit_gps.GPS(self.uart)
        self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        self.gps.send_command(b'PMTK220,1000')

    def __del__(self):
        print("Stopping thread GPS")
        self.wait()

    def run(self):
        while True:
            # using dummy data for now
            # TODO: add function to read correct GPS data
            self.gps.update()
            if not self.gps.has_fix:
                print('Waiting for GPS data...')
                gps_str = ""
                self.gps_updated.emit(str(gps_str))
            else:
                gps_str = "({:.5f}, {:.5f})".format(self.gps.latitude, self.gps.longitude)
                # emit GPS data to the GUI thread that is calling this thread
                self.gps_updated.emit(str(gps_str))
            time.sleep(5.0)
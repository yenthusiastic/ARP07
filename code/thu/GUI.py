import sys
import os
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from SpectrometerGUI import Ui_SpectrometerGUI
#from RTC import RTC
from GPS import GPS
from background_task import *


""" 
Class to render main GUI for application to display data and handle touchscreen inputs
Functions to be included, as defined in Software Architecture:
[X] +initialize(): integer --> __init__(): void
[X] +render_GUI_layout(): integer --> start_GUI(): void
[.] +touch_event_listener(): integer
[ ] +hardware_trigger_listener(): integer
[ ] +display_frame_with_FoV(): integer
[ ] +show_location(): integer
[X] +show_datetime(): integer --> : void
[ ] +update_batt_status(): integer
[ ] +save_data(): integer
[ ] +export_config(): integer
[+.] +show_numpad(): void # show virtual keyboard (numpad) to enter configurations from touchscreen
NOTE: items with [X] means completed, [+] newly added, [.] on-going, [ ] to-do 
"""

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_SpectrometerGUI()
        self.ui.setupUi(self)
        # attach action show_numpad() to Settings button when clicked
        self.ui.settings_btn.clicked.connect(self.show_numpad)
        self.get_datetime()
        self.get_gps()
    
    
    # function to execute a thread which constantly asks for real time
    def get_datetime(self):
        self.rtc_thread = get_PC_time()
        #self.rtc_thread = RTC()
        self.rtc_thread.time_updated.connect(self.show_datetime)
        self.rtc_thread.start()

    # function to execute a thread which constantly asks for GPS location
    def get_gps(self):
        self.gps_thread = GPS()
        self.gps_thread.gps_updated.connect(self.show_location)
        self.gps_thread.start()
    
    # function to display date time on GUI label time_label
    def show_datetime(self, time_str):
        self.ui.time_label.setText("Current date time: {}".format(time_str))
        self.ui.time_label.adjustSize()
    
    # function to display GPS location on GUI label gps_label
    def show_location(self, gps_str):
        self.ui.gps_label.setText("GPS location: {}".format(gps_str))
        self.ui.gps_label.adjustSize()

    # function to show virtual keyboard (numpad) to enter configurations from touchscreen
    def show_numpad(self):
        os.system("matchbox-keyboard")
        # TODO: this causes GUI to hang, have to put in a thread later

def start_GUI():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

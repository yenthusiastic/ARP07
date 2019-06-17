import sys
import os
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from SpectrometerGUI import Ui_SpectrometerGUI
#from RTC import RTC
f#rom GPS import GPS
from background_task import *
from Camera import Camera
import cv2
#from status_led import batt_status_led


""" 
Class to render main GUI for application to display data and handle touchscreen inputs
Functions to be included, as defined in Software Architecture:
[X] +initialize(): integer --> __init__(): void
[X] +render_GUI_layout(): integer --> start_GUI(): void
[-] +touch_event_listener(): integer  --> included in __init__()
[ ] +hardware_trigger_listener(): integer
[.] +display_frame_with_FoV(): integer  --> display_frame(): void
[.] +show_location(): integer --> : void
[X] +show_datetime(): integer --> : void
[.] +update_batt_status(): integer --> show_batt_status(): void
[ ] +save_data(): integer
[ ] +export_config(): integer
[+.] +show_numpad(): void # show virtual keyboard (numpad) to enter configurations from touchscreen
NOTE: items with [X] means completed, [+] newly added, [-] removed, [.] on-going, [ ] to-do 
"""

class MainWindow(QtWidgets.QMainWindow):
    camera_on = True   # boolean to store toggle status of camera
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_SpectrometerGUI()
        self.ui.setupUi(self)
        # set size of camera frame viewport
        self.ui.cam_label.resize(500,300)
        self.ui.cam_label.show() 

        # attach action show_numpad() to Settings button when clicked
        self.ui.settings_btn.clicked.connect(self.show_numpad)
        # attach action toggle_camera() to Camera button when clicked
        self.ui.camera_btn.clicked.connect(self.toggle_camera)

        # initialize all background functions
        self.get_datetime()
        self.toggle_camera()
        #self.get_gps()
        #self.show_batt_status()
    
    # stop the GUI
    def __del__(self):
        print("deleting Main Window")


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

    # function to execute a thread which constantly shows battery status on Neopixel LED
    def show_batt_status(self):
        self.status_led_thread = batt_status_led()
        self.status_led_thread.led_off = False
        self.status_led_thread.start()

    
    # function to switch off Neopixel LED and close all threads upon exit
    def close_all_threads(self):
        self.status_led_thread.led_off = True
        self.camera_thread.camera_on = False
        self.camera_thread.quit()
        self.status_led_thread.quit()
        self.gps_thread.quit()
        self.rtc_thread.quit()
    
    # function to display date time on GUI label time_label
    def show_datetime(self, time_str):
        self.ui.time_label.setText("Current date time: {}".format(time_str))
        self.ui.time_label.adjustSize()
    
    # function to display GPS location on GUI label gps_label
    def show_location(self, gps_str):
        self.ui.gps_label.setText("GPS location: {}".format(gps_str))
        self.ui.gps_label.adjustSize()


    # function to toggle camera display on GUI
    def toggle_camera(self):
        if self.camera_on:
            self.camera_thread = Camera()
            self.camera_thread.camera_on = True
            self.camera_thread.frame_updated.connect(self.display_frame)
            self.camera_thread.start()
            self.ui.camera_btn.setText("Camera off")     
        else: 
            self.ui.camera_btn.setText("Camera on") 
            self.camera_thread.camera_on = False
            self.ui.cam_label.setText("Camera disabled")
            self.ui.cam_label.update()
        self.camera_on = not self.camera_on

    # function to display camera frame on GUI viewport element
    def display_frame(self, frame):
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        img = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.ui.cam_label.setPixmap(QtGui.QPixmap(img))
        self.ui.cam_label.show() 
        

    # function to show virtual keyboard (numpad) to enter configurations from touchscreen
    def show_numpad(self):
        os.system("matchbox-keyboard")
        # TODO: this causes GUI to hang, have to put in a thread later

def start_GUI():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.aboutToQuit.connect(window.close_all_threads)
    sys.exit(app.exec_())




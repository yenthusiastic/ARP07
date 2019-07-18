import sys
import os
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread

from SpectrometerGUI import Ui_SpectrometerGUI
from SettingsUI import Ui_Settings
import os
from background_task import *
#enable following imports if RTC, GPS, Camera, Trigger, Neopixel are available
#from RTC import RTC
#from GPS import GPS
from Camera import Camera
#from status_led import status_led
import numpy as np
from PIL import Image
#import RPi.GPIO as GPIO



""" 
Class to render main GUI for application to display data and handle touchscreen inputs
Functions to be included, as defined in Software Architecture:
[X] +initialize(): integer --> __init__(): void
[X] +render_GUI_layout(): integer --> start_GUI(): void
[X] +touch_event_listener(): integer  --> included in __init__()
[X] +hardware_trigger_listener(): integer --> get_trigger_state(): void
[X] +display_frame_with_FoV(): integer  --> display_frame(): void
[X] +show_location(): integer --> : void
[X] +show_datetime(): integer --> : void
[X] +update_batt_status(): integer --> show_batt_status(): void
[ ] +save_data(): integer
[ ] +export_config(): integer
[+] +show_numpad(): void # show virtual keyboard (numpad) to enter configurations from touchscreen
NOTE: items with [X] means completed, [+] newly added, [-] removed, [.] on-going, [ ] to-do 
"""
TRIGGER_PIN = 16
class MainWindow(QtWidgets.QMainWindow):
    camera_on = True  #boolean to store toggle state of camera capture
   
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_SpectrometerGUI()
        self.ui.setupUi(self)
        
        # initialize list of all child dialogs 
        self.dialogs = list()

        # attach action show_settings() to Settings button when clicked
        self.ui.settings_btn.clicked.connect(self.show_settings)
        # attach action capture_frame() to Camera button when clicked
        # uncomment following if camera is available 
        self.ui.camera_btn.clicked.connect(self.toggle_camera)

        # initialize all background functions
        self.get_datetime()

        # uncomment following lines if GPS, Neopixel, Trigger are available
        self.get_gps()
        self.show_batt_data_status()
        
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(TRIGGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(TRIGGER_PIN, GPIO.FALLING, callback=self.trigger_pressed_cb, bouncetime=200)
        self.session_datetime = None
        self.session_data_dir = "data/"
        

    # stop the GUI
    def __del__(self):
        print("deleting Main Window")
        

    def trigger_pressed_cb(self, trigger_pin=None):
        if self.session_datetime is None:
            self.session_datetime = self.current_datetime
            os.mkdir(self.session_data_dir + self.session_datetime)
            os.chdir(self.session_data_dir + self.session_datetime)
            self.trigger_pressed_cb(self)
            print("np",np.version.version)
        else:
            print("Trigger pin {} pressed".format(trigger_pin))
            #print(self.ui.ydata)
            #print(self.current_datetime)
            #print(self.curent_location)
            np.savetxt(self.current_datetime + ".csv", self.ui.ydata, delimiter=",", fmt='%.0f')
            with open(self.current_datetime + ".csv",'a') as f:
                f.writelines("GPS," + str(self.curent_location) + "\n")
                f.writelines("timestamp," + self.current_datetime + "\n")
            #self.capture_frame(self)


    # function to execute a thread which constantly asks for real time
    def get_datetime(self):
        try:
            self.rtc_thread = RTC() 
            self.rtc_thread.time_updated.connect(self.show_datetime)
            self.rtc_thread.start()
        except Exception as ex:
            print("Error {}: {}".format(type(ex), ex.args))
            self.rtc_thread = get_PC_time()  #use PC time instead
        

    # function to execute a thread which constantly asks for GPS location
    def get_gps(self):
        try:
            self.gps_thread = GPS()
            self.gps_thread.gps_updated.connect(self.show_location)
            self.gps_thread.start()  
        except Exception as ex:
            print("Error {}: {}".format(type(ex), ex.args))
            self.ui.gps_label.setText("Cannot connect to GPS module");     

    # function to execute a thread which constantly shows battery and data status on Neopixel LED
    def show_batt_data_status(self):
        try:
            self.status_led_thread = status_led()
            self.status_led_thread.led_off = False
            self.status_led_thread.batt_data_updated.connect(self.show_batt_level)
            self.status_led_thread.start()
        except Exception as ex:
            print("Error {}: {}".format(type(ex), ex.args))
            self.ui.batt_label.setText("Batt: NA")
            self.ui.data_label.setText("Data: NA")

    def show_batt_level(self, batt_data_value):
        self.ui.batt_label.setText("Batt: {}".format(batt_data_value[0]))
        self.ui.data_label.setText("Data: {}".format(batt_data_value[1]))
        self.ui.batt_label.adjustSize()
        self.ui.data_label.adjustSize()
    
    # function to display date time on GUI label time_label
    def show_datetime(self, time_str):
        self.current_datetime = time_str
        self.ui.time_label.setText("Current date time: {}".format(time_str))
        self.ui.time_label.adjustSize()
    
    # function to display GPS location on GUI label gps_label
    def show_location(self, gps_str):
        if gps_str is not "":
            self.curent_location = gps_str
            self.ui.gps_label.setText("GPS location: {}". format(gps_str))
        else: 
            self.curent_location = None
            self.ui.gps_label.setText("Waiting for GPS data...")
        self.ui.gps_label.adjustSize()

    # function to capture single camera frame
    def toggle_camera(self):
        if self.camera_on:
            # set size of camera frame viewport
            self.ui.cam_label.resize(430,250)
            self.camera_thread = Camera()
            self.camera_thread.camera_on = True
            self.camera_thread.frame_updated.connect(self.display_frame)
            self.camera_thread.start()
        else: 
            self.ui.cam_label.resize(0,0)
            img = QtGui.QImage((0), 0, 0, 0, QtGui.QImage.Format_RGB888)
            self.ui.cam_label.setPixmap(QtGui.QPixmap(img))
            self.camera_thread.camera_on = False
            self.ui.cam_label.lower()
            self.ui.cam_label.show()
            self.ui.graphWidget.raise_()
        self.camera_on = not self.camera_on
          

    # function to display camera frame on GUI viewport element
    def display_frame(self, frame):
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        img = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        self.ui.cam_label.setPixmap(QtGui.QPixmap(img))
        self.ui.cam_label.raise_()
        self.ui.cam_label.show() 
        
        

    # function to show virtual keyboard (numpad) to enter configurations from touchscreen
    def show_settings(self):
        # NOTE: The Keyboard does not work very well when executed from GUI, better use the bash executable from Desktop
        #MBKeyboard().start()
        widget = SettingsWindow()
        self.dialogs.append(widget)
        widget.show()
        


    # function to switch off Neopixel LED and close all threads upon exit
    def close_all_threads(self):
        self.status_led_thread.led_off = True 
        self.status_led_thread.quit()
        self.gps_thread.quit()
        self.rtc_thread.quit()


# class to display the Settings dialog to configure parameters for spectrometers
class SettingsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.ui.spect_range_sldr.valueChanged.connect(self.update_spect_range)
        self.ui.int_time_sldr.valueChanged.connect(self.update_int_time)
        self.ui.acq_burst_sldr.valueChanged.connect(self.update_acq_burst)
        self.ui.ok_btn.clicked.connect(self.update_configs)
        self.spect_range = 190
        self.int_time = 1
        self.acq_burst = 1

    # function to show value of Spectrometer range slider on screen
    def update_spect_range(self):
        self.spect_range = self.ui.spect_range_sldr.value() * 10
        self.ui.spect_range_val.setText("{} nm".format(self.spect_range))

    # function to show value of Integration time slider on screen
    def update_int_time(self):
        if self.ui.int_time_sldr.value() < 1:
            self.int_time = 1
        else:
            self.int_time = self.ui.int_time_sldr.value() * 100
        self.ui.int_time_val.setText("{} ms".format(self.int_time))
            

    # function to show value of Acqusition burst slider on screen
    def update_acq_burst(self):
        if self.ui.acq_burst_sldr.value() < 1:
            self.acq_burst = 1
        else:
            self.acq_burst = self.ui.acq_burst_sldr.value() * 10
        self.ui.acq_burst_val.setText("{}".format(self.acq_burst))
    
    # OK button is pressed,
    # get all user-defined settings parameters and pass to function that set the configs for the spectrometer
    # and close the Settings dialog
    def update_configs(self):
        print("New values: {} nm, {} ms, {}".format(self.spect_range, self.int_time, self.acq_burst))
        #TODO: call function to set parameters for the spectrometers here
        #self.ui.
        
        self.destroy()

        
# function to render GUI layout
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.aboutToQuit.connect(window.close_all_threads)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

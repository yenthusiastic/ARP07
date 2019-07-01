import sys
import os
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from SpectrometerGUI import Ui_SpectrometerGUI
from SettingsUI import Ui_Settings
import os
from background_task import *
#enable following imports if RTC, GPS, Camera, Trigger, Neopixel are available
from RTC import RTC
from GPS import GPS
from Camera import Camera
from Trigger import trigger_reader
from status_led import status_led
import numpy as np
from PIL import Image



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

class MainWindow(QtWidgets.QMainWindow):
    img_name = 'cap.png'
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_SpectrometerGUI()
        self.ui.setupUi(self)
        # set size of camera frame viewport
        self.ui.cam_label.resize(500,300)
        self.ui.cam_label.show() 

        # initialize list of all child dialogs 
        self.dialogs = list()

        # attach action show_settings() to Settings button when clicked
        self.ui.settings_btn.clicked.connect(self.show_settings)
        # attach action capture_frame() to Camera button when clicked
        # uncomment following if camera is available 
        self.ui.camera_btn.clicked.connect(self.capture_frame)

        # initialize all background functions
        self.get_datetime()

        # uncomment following lines if GPS, Neopixel, Trigger are available
        self.get_gps()
        self.show_batt_data_status()
        self.get_trigger_state()
    
    # stop the GUI
    def __del__(self):
        print("deleting Main Window")


    # function to execute a thread which constantly asks for real time
    def get_datetime(self):
        #self.rtc_thread = get_PC_time()  #use PC time, comment if RTC available
        self.rtc_thread = RTC()         #uncomment if RTC available
        self.rtc_thread.time_updated.connect(self.show_datetime)
        self.rtc_thread.start()

    # function to execute a thread which constantly asks for GPS location
    def get_gps(self):
        self.gps_thread = GPS()
        self.gps_thread.gps_updated.connect(self.show_location)
        self.gps_thread.start()        

    # function to execute a thread which constantly shows battery and data status on Neopixel LED
    def show_batt_data_status(self):
        self.status_led_thread = status_led()
        self.status_led_thread.led_off = False
        self.status_led_thread.batt_data_updated.connect(self.show_batt_level)
        self.status_led_thread.start()

    def show_batt_level(self, batt_data_value):
        self.ui.batt_label.setText("Batt: {}".format(batt_data_value[0]))
        self.ui.data_label.setText("Data: {}".format(batt_data_value[1]))
        self.ui.batt_label.adjustSize()
        self.ui.data_label.adjustSize()
    
    # function to display date time on GUI label time_label
    def show_datetime(self, time_str):
        self.ui.time_label.setText("Current date time: {}".format(time_str))
        self.ui.time_label.adjustSize()
    
    # function to display GPS location on GUI label gps_label
    def show_location(self, gps_str):
        self.ui.gps_label.setText(gps_str)
        self.ui.gps_label.adjustSize()

    # function to capture single camera frame
    def capture_frame(self):
        self.ui.cam_label.setText("Capturing camera frame. Please wait...")
        self.camera_thread = Camera()
        self.camera_thread.frame_updated.connect(self.display_frame)
        self.camera_thread.start()
          

    # function to display camera frame on GUI viewport element
    def display_frame(self, exit_code):
        if exit_code == 0:
            img = Image.open(self.img_name)
            img.load()
            frame = np.asarray(img)
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            img = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
            self.ui.cam_label.setPixmap(QtGui.QPixmap(img))
            self.ui.cam_label.show() 
        else:
            print("Unable to load", self.img_name)
            self.ui.cam_label.setText("Error: Camera unavailable")
        
        

    # function to show virtual keyboard (numpad) to enter configurations from touchscreen
    def show_settings(self):
        # NOTE: The Keyboard does not work very well when executed from GUI, better use the bash executable from Desktop
        #MBKeyboard().start()
        widget = SettingsWindow()
        self.dialogs.append(widget)
        widget.show()
        
        
    # function to read trigger state 
    def get_trigger_state(self):
        self.trigger_thread = trigger_reader()
        self.trigger_thread.trigger_updated.connect(self.capture_frame)
        self.trigger_thread.start()


    # function to switch off Neopixel LED and close all threads upon exit
    def close_all_threads(self):
        self.status_led_thread.led_off = True 
        self.status_led_thread.quit()
        self.gps_thread.quit()
        self.rtc_thread.quit()

# function to render GUI layout
def start_GUI():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.aboutToQuit.connect(window.close_all_threads)
    sys.exit(app.exec_())


# class to display virtual keyboard (numpad) for touchscreen
class MBKeyboard(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()
    
    def run(self):
        os.system("matchbox-keyboard")



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
        self.destroy()

        
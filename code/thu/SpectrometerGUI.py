# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph as pg
import seabreeze
seabreeze.use("cseabreeze")
import seabreeze.spectrometers as sb

import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
plt.ion()
import seabreeze.backends
lib = seabreeze.backends.get_backend()

TRIGGER_PIN = 16

def init_spectrometers():
    print("Looking for spectrometer devices...")
    devices = sb.list_devices()
    print(devices)
    
    lib.device_close(devices[0])
    lib.device_close(devices[1])

    try:
        return sb.Spectrometer(devices[0]), sb.Spectrometer(devices[1])
    except:
        print("Can't connect to two Spectrometers.")


def set_int_time(int_time):
    spec_1.integration_time_micros(int_time)
    spec_2.integration_time_micros(int_time)
    

def auto_int_time():
    # Existing Code too slow Re-do!
    print("TBD...")

def measure_avg(dc=0, avg_num=10):
    avg_1 = np.around(spec_1.intensities()).astype(int)
    avg_2 = np.around(spec_2.intensities()).astype(int)
    for i in range(avg_num - 1):
        avg_1 = np.add(avg_1, np.around(spec_1.intensities()).astype(int))
        avg_2 = np.add(avg_2, np.around(spec_2.intensities()).astype(int))
    avg_1 = np.around(np.true_divide(avg_1, avg_num)).astype(int)
    avg_2 = np.around(np.true_divide(avg_2, avg_num)).astype(int)
    return avg_1 - dc, avg_2 - dc

def measure_dc(avg_num=20):
    dc_1, dc_2 = measure_avg(avg_num=avg_num)
    return dc_1, dc_2

def measure_raw(dc=0):
    raw_1 = spec_1.intensities()
    raw_2 = spec_2.intensities()
    return raw_1 - dc, raw_2 - dc

def measure_raw_avg(dc=0, avg_num=2):
    raw_1, raw_2 = measure_avg(avg_num=avg_num)
    return raw_1 - dc, raw_2 - dc

def measure_ref(ref_1, ref_2, dc=0, avg_num=0):
    if avg == 0:
        raw_1, raw_2 = measure_raw(dc=dc)
    else:
        avg_1, avg_2 = measure_avg(dc=dc, avg_num=avg_num)
    ref_1 = np.true_divide(raw_1,ref_1)
    ref_2 = np.true_divide(raw_2,ref_2)
    return ref_1, ref_2

def calibrate_ref(dc=0, avg_num=10):
    ref_1, ref_2 = measure_avg(avg_num=avg_num)
    return ref_1 - dc, ref_2 - dc

def get_wavelenghts():
    wl_1 = spec_1.wavelengths()
    wl_2 = spec_2.wavelengths()
    return wl_1, wl_2

spec_2, spec_1 =  init_spectrometers()
set_int_time(240000)

class Ui_SpectrometerGUI(object):
    def setupUi(self, SpectrometerGUI):
        SpectrometerGUI.setObjectName("SpectrometerGUI")
        SpectrometerGUI.resize(720, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpectrometerGUI.sizePolicy().hasHeightForWidth())
        SpectrometerGUI.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        SpectrometerGUI.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SpectrometerGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.camera_btn = QtWidgets.QPushButton(self.centralwidget)
        self.camera_btn.setGeometry(QtCore.QRect(540, 140, 150, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_btn.sizePolicy().hasHeightForWidth())
        self.camera_btn.setSizePolicy(sizePolicy)
        self.camera_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.camera_btn.setFont(font)
        self.camera_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_btn.setDefault(False)
        self.camera_btn.setFlat(False)
        self.camera_btn.setProperty("pressed", False)
        self.camera_btn.setObjectName("camera_btn")
        self.cal_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cal_btn.setGeometry(QtCore.QRect(540, 210, 150, 60))
        self.cal_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.cal_btn.setFont(font)
        self.cal_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cal_btn.setObjectName("cal_btn")
        self.settings_btn = QtWidgets.QToolButton(self.centralwidget)
        self.settings_btn.setGeometry(QtCore.QRect(540, 350, 150, 60))
        self.settings_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.settings_btn.setFont(font)
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn.setObjectName("settings_btn")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(540, 280, 150, 60))
        self.start_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setObjectName("start_btn")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(15, 50, 267, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        self.time_label.setMinimumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.gps_label = QtWidgets.QLabel(self.centralwidget)
        self.gps_label.setGeometry(QtCore.QRect(15, 90, 511, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gps_label.sizePolicy().hasHeightForWidth())
        self.gps_label.setSizePolicy(sizePolicy)
        self.gps_label.setMinimumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.gps_label.setFont(font)
        self.gps_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gps_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gps_label.setObjectName("gps_label")
        self.cam_label = QtWidgets.QLabel(self.centralwidget)
        self.cam_label.setGeometry(QtCore.QRect(10, 120, 265, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cam_label.setFont(font)
        self.cam_label.setObjectName("cam_label")

        #### Create Gui Elements ###########
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.graphWidget = pg.Qt.QtGui.QWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(10, 150, 500, 300))
        self.graphWidget.setLayout(QtGui.QVBoxLayout())

        self.canvas = pg.GraphicsLayoutWidget()
        self.graphWidget.layout().addWidget(self.canvas)

        self.label = QtWidgets.QLabel()
        self.graphWidget.layout().addWidget(self.label)

        #  line plot
        self.otherplot = self.canvas.addPlot()

        # Set Ticks test - display too small!
        # self.ax=self.otherplot.getAxis('bottom')
        # wl_1, wl_2 = get_wavelenghts()
        # tmp_raw = np.concatenate((np.delete(wl_1,[0,1]),wl_2), axis=None)
        # tmp_list = np.around(tmp_raw, decimals=0).astype(int).tolist()
        # tmp_list_str = list(map(str, tmp_list))
        # tmp_list_nth = tmp_list[0::100]
        # list_nth_num = range(2173)
        # list_nth_num = list_nth_num[0::100]
        # xdict = dict(zip(list_nth_num, tmp_list_nth))
        # print(xdict)
        # self.ax.setTicks([xdict.items()])

        self.otherplot.setRange(yRange=[0,65535])
        self.otherplot.setRange(xRange=[0,2173]) # 2028 + 128 - 2
        self.h2 = self.otherplot.plot(pen="k")
        # Add a line to seperate both Spectrometer data.
        # Note: x is 2046 since we are deleting the first two entries in the spec_1 array due to high noise
        self.otherplot.addLine(x=2046, y=[0,65535], pen='r')

        self.counter = 0
        self.fps = 0.
        self.lastupdate = time.time()
        self.showFPS = True

        # Mode flag. Options: "raw" , "ref"
        self.mode_flag = "raw"
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(TRIGGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(TRIGGER_PIN, GPIO.FALLING, callback=self.int_handler, bouncetime=200)

        #### Start  #####################
        self._update()

        self.batt_label = QtWidgets.QLabel(self.centralwidget)
        self.batt_label.setGeometry(QtCore.QRect(350, 10, 70, 35))
        self.batt_label.setObjectName("batt_label")
        self.data_label = QtWidgets.QLabel(self.centralwidget)
        self.data_label.setGeometry(QtCore.QRect(550, 10, 75, 35))
        self.data_label.setObjectName("data_label")
        SpectrometerGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SpectrometerGUI)
        self.statusbar.setObjectName("statusbar")
        SpectrometerGUI.setStatusBar(self.statusbar)
        self.config_action = QtWidgets.QAction(SpectrometerGUI)
        self.config_action.setObjectName("config_action")
        self.ref_action = QtWidgets.QAction(SpectrometerGUI)
        self.ref_action.setObjectName("ref_action")
        self.retranslateUi(SpectrometerGUI)
        QtCore.QMetaObject.connectSlotsByName(SpectrometerGUI)

        



    def retranslateUi(self, SpectrometerGUI):
        _translate = QtCore.QCoreApplication.translate
        SpectrometerGUI.setWindowTitle(_translate("SpectrometerGUI", "Spectrometer GUI"))
        self.camera_btn.setText(_translate("SpectrometerGUI", "Capture"))
        self.cal_btn.setText(_translate("SpectrometerGUI", "Calibrate"))
        self.settings_btn.setText(_translate("SpectrometerGUI", "Settings"))
        self.start_btn.setText(_translate("SpectrometerGUI", "Start"))
        self.time_label.setText(_translate("SpectrometerGUI", "Current date time:"))
        self.gps_label.setText(_translate("SpectrometerGUI", "GPS location: 51.4910482, 6.5350449"))
        #self.cam_label.setText(_translate("SpectrometerGUI", "Camera disabled."))
        self.batt_label.setText(_translate("SpectrometerGUI", "Batt:"))
        self.data_label.setText(_translate("SpectrometerGUI", "Data:"))
        self.config_action.setText(_translate("SpectrometerGUI", "Load configurations"))
        self.ref_action.setText(_translate("SpectrometerGUI", "Preferences"))


    def int_handler(self, channel):
        print("interrupt handler")

    def display(self):
        #print("placeholder")
        if self.mode_flag == "raw":
           print("raw mode")
        elif self.mode_flag == "ref":
            print("ref mode")

    def _update(self):
        #self.ydata = np.concatenate((np.delete(spec_1.intensities(),[0,1]),spec_2.intensities()), axis=None) # subtract dark current
        #self.display()
        meas_1, meas_2 = measure_raw()
        self.ydata = np.concatenate((np.delete(meas_1,[0,1]),meas_2), axis=None) # subtract dark current
        self.h2.setData(self.ydata)

        if self.showFPS:
            now = time.time()
            dt = (now-self.lastupdate)
            if dt <= 0:
                dt = 0.000000000001
            fps2 = 1.0 / dt
            self.lastupdate = now
            self.fps = self.fps * 0.9 + fps2 * 0.1
            tx = 'Mean Frame Rate:  {fps:.3f} FPS'.format(fps=self.fps )
            self.label.setText(tx)
            QtCore.QTimer.singleShot(10, self._update)
            self.counter += 1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpectrometerGUI = QtWidgets.QMainWindow()
    ui = Ui_SpectrometerGUI()
    ui.setupUi(SpectrometerGUI)
    SpectrometerGUI.show()
    sys.exit(app.exec_())


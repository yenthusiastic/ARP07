import sys
import time
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph as pg


import seabreeze
## Backend options:
# "cseabreeze" C++ Wrapper for ocean optics API (fast and supports more spectrometer models)
# "pyseabreeze" Python Wrapper for ocean optics API (slower and doesnt support all spectrometers)
seabreeze.use("cseabreeze")
import seabreeze.spectrometers as sb

import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

def init_spectrometers():
    devices = sb.list_devices()
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
set_int_time(120000)

class App(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        #### Create Gui Elements ###########
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.mainbox = QtGui.QWidget()
        self.setCentralWidget(self.mainbox)
        self.mainbox.setLayout(QtGui.QVBoxLayout())

        self.canvas = pg.GraphicsLayoutWidget()
        self.mainbox.layout().addWidget(self.canvas)

        self.label = QtGui.QLabel()
        self.mainbox.layout().addWidget(self.label)

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
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(14, GPIO.FALLING, callback=self.int_handler, bouncetime=200)

        #### Start  #####################
        self._update()

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

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    thisapp = App()
    thisapp.show()
    sys.exit(app.exec_())

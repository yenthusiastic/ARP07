import sys
from PyQt5 import QtCore, QtWidgets, uic
from SpectrometerGUI import Ui_SpectrometerGUI


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_SpectrometerGUI()
        self.ui.setupUi(self)
        # self.ui.start_btn.clicked.connect(self.set_datetime)
        # self.ui.start_btn.clicked.connect(self.set_loc)
    
    def set_datetime(self):
        self.ui.time_label.setText("Current date time: {}".format("test1"))
        self.ui.time_label.adjustSize()
    
    def set_loc(self):
        self.ui.gps_label.setText("GPS location: {}".format("test2"))
        self.ui.gps_label.adjustSize()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
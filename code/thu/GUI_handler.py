import sys
from PyQt5 import QtCore, QtWidgets, uic
from SpectrometerGUI import Ui_SpectrometerGUI
from background_task_handler import get_RTC

# Functions to be included, as defined in Software Architecture:
# [X] +initialize(): integer --> __inti__(): void
# [X] +render_GUI_layout(): integer --> start_GUI(): void
# [ ] +touch_event_listener(): integer
# [ ] +hardware_trigger_listener(): integer
# [ ] +display_frame_with_FoV(): integer
# [ ] +show_location(): integer
# [ ] +show_datetime(): integer
# [ ] +update_batt_status(): integer
# [ ] +save_data(): integer
# [ ] +export_config(): integer
# NOTE: items with [X] means checked, else means to-do

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_SpectrometerGUI()
        self.ui.setupUi(self)
        self.ui.start_btn.clicked.connect(self.set_datetime)
        self.ui.start_btn.clicked.connect(self.set_loc)
        self.rtc_thread = get_RTC()
        self.rtc_thread.start()
    
    def set_datetime(self):
        self.ui.time_label.setText("Current date time: {}".format("test1"))
        self.ui.time_label.adjustSize()
    
    def set_loc(self):
        self.ui.gps_label.setText("GPS location: {}".format("test2"))
        self.ui.gps_label.adjustSize()


def start_GUI():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

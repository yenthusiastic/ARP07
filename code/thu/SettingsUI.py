# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(400, 300)
        self.spect_range_sldr = QtWidgets.QSlider(Settings)
        self.spect_range_sldr.setGeometry(QtCore.QRect(220, 45, 160, 22))
        self.spect_range_sldr.setOrientation(QtCore.Qt.Horizontal)
        self.spect_range_sldr.setObjectName("spect_range_sldr")
        self.label1 = QtWidgets.QLabel(Settings)
        self.label1.setGeometry(QtCore.QRect(10, 34, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(Settings)
        self.label2.setGeometry(QtCore.QRect(10, 116, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.int_time_sldr = QtWidgets.QSlider(Settings)
        self.int_time_sldr.setGeometry(QtCore.QRect(220, 124, 160, 22))
        self.int_time_sldr.setOrientation(QtCore.Qt.Horizontal)
        self.int_time_sldr.setObjectName("int_time_sldr")
        self.label3 = QtWidgets.QLabel(Settings)
        self.label3.setGeometry(QtCore.QRect(10, 195, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.acq_burst_sldr = QtWidgets.QSlider(Settings)
        self.acq_burst_sldr.setGeometry(QtCore.QRect(220, 200, 160, 22))
        self.acq_burst_sldr.setOrientation(QtCore.Qt.Horizontal)
        self.acq_burst_sldr.setObjectName("acq_burst_sldr")
        self.ok_btn = QtWidgets.QPushButton(Settings)
        self.ok_btn.setGeometry(QtCore.QRect(160, 250, 93, 28))
        self.ok_btn.setObjectName("ok_btn")
        self.spect_range_val = QtWidgets.QLabel(Settings)
        self.spect_range_val.setGeometry(QtCore.QRect(260, 21, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spect_range_val.setFont(font)
        self.spect_range_val.setObjectName("spect_range_val")
        self.int_time_val = QtWidgets.QLabel(Settings)
        self.int_time_val.setGeometry(QtCore.QRect(270, 96, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.int_time_val.setFont(font)
        self.int_time_val.setObjectName("int_time_val")
        self.acq_burst_val = QtWidgets.QLabel(Settings)
        self.acq_burst_val.setGeometry(QtCore.QRect(290, 180, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.acq_burst_val.setFont(font)
        self.acq_burst_val.setObjectName("acq_burst_val")

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.label1.setText(_translate("Settings", "Spectral range"))
        self.label2.setText(_translate("Settings", "Integration time"))
        self.label3.setText(_translate("Settings", "Acquisition burst"))
        self.ok_btn.setText(_translate("Settings", "OK"))
        self.spect_range_val.setText(_translate("Settings", "600 nm"))
        self.int_time_val.setText(_translate("Settings", "10 ms"))
        self.acq_burst_val.setText(_translate("Settings", "5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpectrometerGUI(object):
    def setupUi(self, SpectrometerGUI):
        SpectrometerGUI.setObjectName("SpectrometerGUI")
        SpectrometerGUI.resize(800, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpectrometerGUI.sizePolicy().hasHeightForWidth())
        SpectrometerGUI.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(SpectrometerGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.viewport = QtWidgets.QGraphicsView(self.centralwidget)
        self.viewport.setGeometry(QtCore.QRect(50, 100, 500, 300))
        self.viewport.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewport.setObjectName("viewport")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 210, 201, 16))
        self.label.setObjectName("label")
        self.camera_btn = QtWidgets.QPushButton(self.centralwidget)
        self.camera_btn.setGeometry(QtCore.QRect(600, 120, 150, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_btn.sizePolicy().hasHeightForWidth())
        self.camera_btn.setSizePolicy(sizePolicy)
        self.camera_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.camera_btn.setFont(font)
        self.camera_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.camera_btn.setObjectName("camera_btn")
        self.spect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.spect_btn.setGeometry(QtCore.QRect(600, 190, 150, 40))
        self.spect_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.spect_btn.setFont(font)
        self.spect_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spect_btn.setObjectName("spect_btn")
        self.settings_btn = QtWidgets.QToolButton(self.centralwidget)
        self.settings_btn.setGeometry(QtCore.QRect(600, 330, 150, 40))
        self.settings_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.settings_btn.setFont(font)
        self.settings_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settings_btn.setObjectName("settings_btn")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(600, 260, 150, 40))
        self.start_btn.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        self.time_label.setMinimumSize(QtCore.QSize(220, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout.addWidget(self.time_label)
        self.gps_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gps_label.sizePolicy().hasHeightForWidth())
        self.gps_label.setSizePolicy(sizePolicy)
        self.gps_label.setMinimumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gps_label.setFont(font)
        self.gps_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.gps_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gps_label.setObjectName("gps_label")
        self.horizontalLayout.addWidget(self.gps_label)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        SpectrometerGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpectrometerGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 37))
        self.menubar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        SpectrometerGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpectrometerGUI)
        self.statusbar.setObjectName("statusbar")
        SpectrometerGUI.setStatusBar(self.statusbar)
        self.config_action = QtWidgets.QAction(SpectrometerGUI)
        self.config_action.setObjectName("config_action")
        self.ref_action = QtWidgets.QAction(SpectrometerGUI)
        self.ref_action.setObjectName("ref_action")
        self.menuFile.addAction(self.config_action)
        self.menuFile.addAction(self.ref_action)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(SpectrometerGUI)
        QtCore.QMetaObject.connectSlotsByName(SpectrometerGUI)

    def retranslateUi(self, SpectrometerGUI):
        _translate = QtCore.QCoreApplication.translate
        SpectrometerGUI.setWindowTitle(_translate("SpectrometerGUI", "Spectrometer GUI"))
        self.label.setText(_translate("SpectrometerGUI", "Frame capture from camera"))
        self.camera_btn.setText(_translate("SpectrometerGUI", "Camera"))
        self.spect_btn.setText(_translate("SpectrometerGUI", "Spectrum"))
        self.settings_btn.setText(_translate("SpectrometerGUI", "Settings"))
        self.start_btn.setText(_translate("SpectrometerGUI", "Start"))
        self.time_label.setText(_translate("SpectrometerGUI", "Current date time:"))
        self.gps_label.setText(_translate("SpectrometerGUI", "GPS location:"))
        self.menuFile.setTitle(_translate("SpectrometerGUI", "File"))
        self.config_action.setText(_translate("SpectrometerGUI", "Load configurations"))
        self.ref_action.setText(_translate("SpectrometerGUI", "Preferences"))


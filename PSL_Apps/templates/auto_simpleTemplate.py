# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simpleTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widgetFrameOuter = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetFrameOuter.sizePolicy().hasHeightForWidth())
        self.widgetFrameOuter.setSizePolicy(sizePolicy)
        self.widgetFrameOuter.setStyleSheet("")
        self.widgetFrameOuter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.widgetFrameOuter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.widgetFrameOuter.setObjectName("widgetFrameOuter")
        self.gridLayout = QtWidgets.QGridLayout(self.widgetFrameOuter)
        self.gridLayout.setContentsMargins(0, 3, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(10, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.ControlsLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.ControlsLayout.setContentsMargins(0, 0, 0, 0)
        self.ControlsLayout.setSpacing(3)
        self.ControlsLayout.setObjectName("ControlsLayout")
        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.frame = QtWidgets.QFrame(self.widgetFrameOuter)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WidgetLayout = QtWidgets.QHBoxLayout()
        self.WidgetLayout.setObjectName("WidgetLayout")
        self.verticalLayout.addLayout(self.WidgetLayout)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.widgetFrameOuter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 828, 490))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.plot_area = QtWidgets.QGridLayout()
        self.plot_area.setHorizontalSpacing(0)
        self.plot_area.setVerticalSpacing(3)
        self.plot_area.setObjectName("plot_area")
        self.gridLayout_4.addLayout(self.plot_area, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.widgetFrameOuter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.widgetFrameOuter.setProperty("class", _translate("MainWindow", "PeripheralCollection"))
        self.frame_2.setProperty("class", _translate("MainWindow", "PeripheralCollectionInner"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

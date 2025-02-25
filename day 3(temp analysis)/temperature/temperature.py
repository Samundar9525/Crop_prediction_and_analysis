# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temperature.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 655)
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 151, 641))
        self.frame.setStyleSheet("background-color: rgb(0, 1, 86);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 71, 61))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/logo2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 145, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 180, 145, 220))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(35, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(35, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(35, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(150, 0, 681, 641))
        self.frame_2.setStyleSheet("background-color: rgb(0, 93, 93);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.templabel = QtWidgets.QLabel(self.frame_2)
        self.templabel.setGeometry(QtCore.QRect(190, 10, 281, 51))
        self.templabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.templabel.setObjectName("templabel")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 150, 571, 61))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 0, 150, 16))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(60, 30, 45, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(250, 30, 45, 16))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(420, 30, 61, 16))
        self.label_10.setObjectName("label_10")
        self.todaymax = QtWidgets.QLabel(self.frame_3)
        self.todaymax.setGeometry(QtCore.QRect(100, 30, 45, 16))
        self.todaymax.setObjectName("todaymax")
        self.todaymin = QtWidgets.QLabel(self.frame_3)
        self.todaymin.setGeometry(QtCore.QRect(290, 30, 45, 16))
        self.todaymin.setObjectName("todaymin")
        self.todayhumidity = QtWidgets.QLabel(self.frame_3)
        self.todayhumidity.setGeometry(QtCore.QRect(490, 30, 45, 16))
        self.todayhumidity.setObjectName("todayhumidity")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(50, 270, 571, 61))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 150, 16))
        self.label_4.setObjectName("label_4")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(60, 30, 45, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(250, 30, 45, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(420, 30, 61, 16))
        self.label_16.setObjectName("label_16")
        self.day1max = QtWidgets.QLabel(self.frame_4)
        self.day1max.setGeometry(QtCore.QRect(100, 30, 45, 16))
        self.day1max.setObjectName("day1max")
        self.day1min = QtWidgets.QLabel(self.frame_4)
        self.day1min.setGeometry(QtCore.QRect(290, 30, 45, 16))
        self.day1min.setObjectName("day1min")
        self.day1humidity = QtWidgets.QLabel(self.frame_4)
        self.day1humidity.setGeometry(QtCore.QRect(490, 30, 45, 16))
        self.day1humidity.setObjectName("day1humidity")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(50, 340, 571, 61))
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        self.label_20.setGeometry(QtCore.QRect(10, 0, 150, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(60, 30, 45, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(250, 30, 45, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_23.setGeometry(QtCore.QRect(420, 30, 61, 16))
        self.label_23.setObjectName("label_23")
        self.day2max = QtWidgets.QLabel(self.frame_5)
        self.day2max.setGeometry(QtCore.QRect(100, 30, 45, 16))
        self.day2max.setObjectName("day2max")
        self.day2min = QtWidgets.QLabel(self.frame_5)
        self.day2min.setGeometry(QtCore.QRect(290, 30, 45, 16))
        self.day2min.setObjectName("day2min")
        self.day2humidity = QtWidgets.QLabel(self.frame_5)
        self.day2humidity.setGeometry(QtCore.QRect(490, 30, 45, 16))
        self.day2humidity.setObjectName("day2humidity")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(50, 410, 571, 61))
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(10, 0, 150, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_6)
        self.label_28.setGeometry(QtCore.QRect(60, 30, 45, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_6)
        self.label_29.setGeometry(QtCore.QRect(250, 30, 45, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_6)
        self.label_30.setGeometry(QtCore.QRect(420, 30, 61, 16))
        self.label_30.setObjectName("label_30")
        self.day3max = QtWidgets.QLabel(self.frame_6)
        self.day3max.setGeometry(QtCore.QRect(100, 30, 45, 16))
        self.day3max.setObjectName("day3max")
        self.day3min = QtWidgets.QLabel(self.frame_6)
        self.day3min.setGeometry(QtCore.QRect(290, 30, 45, 16))
        self.day3min.setObjectName("day3min")
        self.day3humidity = QtWidgets.QLabel(self.frame_6)
        self.day3humidity.setGeometry(QtCore.QRect(490, 30, 45, 16))
        self.day3humidity.setObjectName("day3humidity")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setGeometry(QtCore.QRect(50, 480, 571, 61))
        self.frame_7.setAutoFillBackground(False)
        self.frame_7.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.label_34 = QtWidgets.QLabel(self.frame_7)
        self.label_34.setGeometry(QtCore.QRect(10, 0, 150, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_7)
        self.label_35.setGeometry(QtCore.QRect(60, 30, 45, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame_7)
        self.label_36.setGeometry(QtCore.QRect(250, 30, 45, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_7)
        self.label_37.setGeometry(QtCore.QRect(420, 30, 61, 16))
        self.label_37.setObjectName("label_37")
        self.day4max = QtWidgets.QLabel(self.frame_7)
        self.day4max.setGeometry(QtCore.QRect(100, 30, 45, 16))
        self.day4max.setObjectName("day4max")
        self.day4min = QtWidgets.QLabel(self.frame_7)
        self.day4min.setGeometry(QtCore.QRect(290, 30, 45, 16))
        self.day4min.setObjectName("day4min")
        self.day4humidity = QtWidgets.QLabel(self.frame_7)
        self.day4humidity.setGeometry(QtCore.QRect(490, 30, 45, 16))
        self.day4humidity.setObjectName("day4humidity")
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setGeometry(QtCore.QRect(50, 550, 571, 61))
        self.frame_8.setAutoFillBackground(False)
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_8.setObjectName("frame_8")
        self.label_41 = QtWidgets.QLabel(self.frame_8)
        self.label_41.setGeometry(QtCore.QRect(10, 0, 150, 16))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_8)
        self.label_42.setGeometry(QtCore.QRect(60, 30, 45, 16))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_8)
        self.label_43.setGeometry(QtCore.QRect(250, 30, 45, 16))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_8)
        self.label_44.setGeometry(QtCore.QRect(420, 30, 61, 16))
        self.label_44.setObjectName("label_44")
        self.day5max = QtWidgets.QLabel(self.frame_8)
        self.day5max.setGeometry(QtCore.QRect(100, 30, 45, 16))
        self.day5max.setObjectName("day5max")
        self.day5min = QtWidgets.QLabel(self.frame_8)
        self.day5min.setGeometry(QtCore.QRect(290, 30, 45, 16))
        self.day5min.setObjectName("day5min")
        self.day5humidity = QtWidgets.QLabel(self.frame_8)
        self.day5humidity.setGeometry(QtCore.QRect(490, 30, 45, 16))
        self.day5humidity.setObjectName("day5humidity")
        self.label_48 = QtWidgets.QLabel(self.frame_2)
        self.label_48.setGeometry(QtCore.QRect(240, 220, 230, 45))
        self.label_48.setObjectName("label_48")
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setGeometry(QtCore.QRect(50, 100, 571, 41))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_11 = QtWidgets.QLabel(self.frame_9)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.label_11.setObjectName("label_11")
        self.cityoption = QtWidgets.QComboBox(self.frame_9)
        self.cityoption.setGeometry(QtCore.QRect(80, 10, 201, 22))
        self.cityoption.setObjectName("cityoption")
        for i in range (7):          #yahan maine state ka skeleton dala haai
                self.cityoption.addItem("")

        self.temppredict = QtWidgets.QPushButton(self.frame_9)
        self.temppredict.setGeometry(QtCore.QRect(330, 10, 191, 24))
        self.temppredict.setStyleSheet("background-color: rgb(0, 130, 0);\n"
"color: rgb(255, 255, 255);")
        self.temppredict.setObjectName("temppredict")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Weather  dashboard"))
        self.pushButton.setText(_translate("MainWindow", "Rainfall"))
        self.pushButton_2.setText(_translate("MainWindow", "Temperature"))
        self.pushButton_4.setText(_translate("MainWindow", "Cyclone"))
        self.templabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Temperature Prediction</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Today</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MAX</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MIN</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">HUMIDITY</span></p></body></html>"))
        self.todaymax.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.todaymin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.todayhumidity.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Day 1</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MAX</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MIN</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">HUMIDITY</span></p></body></html>"))
        self.day1max.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day1min.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day1humidity.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Day 2</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MAX</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MIN</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">HUMIDITY</span></p></body></html>"))
        self.day2max.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day2min.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day2humidity.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Day 3</span></p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MAX</span></p></body></html>"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MIN</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">HUMIDITY</span></p></body></html>"))
        self.day3max.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day3min.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day3humidity.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Day 4</span></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MAX</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MIN</span></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">HUMIDITY</span></p></body></html>"))
        self.day4max.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day4min.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day4humidity.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Day 5</span></p></body></html>"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MAX</span></p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MIN</span></p></body></html>"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">HUMIDITY</span></p></body></html>"))
        self.day5max.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day5min.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.day5humidity.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.label_48.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700; color:#ffffff;\">Weekly Prediction  </span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Select State"))
        self.temppredict.setText(_translate("MainWindow", "Predict Temperarure"))  #ye mera button hai
#--------------------------------------------------------yahan button ka trigger set kiya ja raha hai------------        
        self.temppredict.pressed.connect(self.func)
#=------------------------------------------------------------------------------------my original work start here-------
        arr = ["Delhi","Jaipur","Pune","Mumbai","Kanpur","Nagpur","Hyderabad"]
        for i in range (len(arr)):
                self.cityoption.setItemText(i, _translate("MainWindow", arr[i]))                 #yahan maine city ka data dala haai

#-------------------------------------------------------------------------------yahan mere functions hai---------
    def func(self):
            citycontent=self.cityoption.currentText()
            self.find(citycontent)


    def find(self,citycontent):
            # yahan par predict karo
            df=pd.read_csv("data/"+citycontent+".csv")
            df.dropna()
            cols=list(df.columns)
            t=df[cols[0:1]]
            a=list(t["date_time"])
            b=[]
            c=[]
            for i in range(len(a)):
                    b.append(a[i][0:10])
                    c.append(a[i][12:17])

            cols=list(df.columns)

            newd=df[cols[1:2]+cols[2:3]+cols[18:19]]

            tem1=pd.DataFrame(data=b,columns=["Date"]) 
            tem2=pd.DataFrame(data=c,columns=["time"]) 
            newdf=pd.concat([tem1,tem2,newd],axis=1)
            
#------------------------yahan linear regression use karke temp rpredict karwa rahe hai ----------------------           
           

            X = np.array(newdf['mintempC']).reshape(-1, 1) 
            y = np.array(newdf['maxtempC']).reshape(-1, 1)

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
            regr = LinearRegression()
            regr.fit(X_train, y_train) 
             
            w1=regr.coef_[0]   # this will hold the value of the slope 
            w0=regr.intercept_
            from datetime import date
            today = date.today()
            res=""

            if(len(str(today.month))==1):
                    res='0'+str(today.month)+'-'
            else:
                    res=str(today.month)+'-'

            if(len(str(today.day))==1):
                    res+='0'+str(today.day)
            else:
                    res+=str(today.day)
            print(res)
            t=newdf.loc[newdf["Date"].str.contains(res)].mean()
            print((t))
           
            exp=t[1]      #yahan apan ne min ka data diya 
            res1=w1*exp+w0
        #     print("Expected max:: ",round(res[0],2))
            exp=t[0] # yahan par apan ne max ka data diya
            res2=(exp-w0)/w1
            self.label.setText("Today : "+str(today))
            self.label.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.todaymax.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.todaymax.setText(str(round(res1[0]))+" °C")
            self.todaymin.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.todaymin.setText(str(round(res2[0]))+" °C")
            self.todayhumidity.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.todayhumidity.setText(str(round(t[2]))+" %")
            
            from datetime import datetime, timedelta 
            def dayfun(today):
                    res=""
                    if len(str(today.month))==1:
                            res='0'+str(today.month)+'-'
                    else:
                            res=str(today.month)+'-'

                    if len(str(today.day))==1:
                            res+='0'+str(today.day)
                    else:
                            res+=str(today.day)
                    return(res)
            day1=today + timedelta(days = 1)
            d1=dayfun(day1)
            label_day1=d1+"-"+str(today.year)

            day2=day1 + timedelta(days = 1)
            d2=dayfun(day2)
            label_day2=d2+"-"+str(today.year)

            day3=day2 + timedelta(days = 1)
            d3=dayfun(day3)
            label_day3=d3+"-"+str(today.year)

            day4=day3 + timedelta(days = 1)
            d4=dayfun(day4)
            label_day4=d4+"-"+str(today.year)

            day5=day4 + timedelta(days = 1)
            d5=dayfun(day5)
            label_day5=d5+"-"+str(today.year)
            
            #print(label_day1,label_day2,label_day3,label_day4,label_day5)

            def predict(ma,mi):
                    exp=mi      #yahan apan ne min ka data diya 
                    res=w1*exp+w0
                    exp=ma # yahan par apan ne max ka data diya
                    res2=(exp-w0)/w1
                    return ([res,res2])
#----------------------day 1 ke liye----------------------------
            t=newdf.loc[newdf["Date"].str.contains(d1)].mean()
            ma=round(t[0])
            mi=round(t[1])
            res1=predict(ma,mi)
            print(res1[0][0],res1[1][0])
            self.label_4.setText("Day 1:  "+str(label_day1))
            self.label_4.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.day1max.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day1max.setText(str(round(res1[0][0]))+" °C")
            self.day1min.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day1min.setText(str(round(res1[1][0]))+" °C")
            self.day1humidity.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day1humidity.setText(str(round(t[2]))+" %")
#----------------------day 2 ke liye----------------------------
            t=newdf.loc[newdf["Date"].str.contains(d2)].mean()
            ma=round(t[0])
            mi=round(t[1])
            res2=predict(ma,mi)
            print(res2[0][0],res2[1][0])
            self.label_20.setText("Day 2:  "+str(label_day2))
            self.label_20.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.day2max.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day2max.setText(str(round(res2[0][0]))+" °C")
            self.day2min.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day2min.setText(str(round(res2[1][0]))+" °C")
            self.day2humidity.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day2humidity.setText(str(round(t[2]))+" %")

#----------------------day 3 ke liye----------------------------
            t=newdf.loc[newdf["Date"].str.contains(d3)].mean()
            ma=round(t[0])
            mi=round(t[1])
            res3=predict(ma,mi)
            print(res3[0][0],res3[1][0])
            self.label_27.setText("Day 3:  "+str(label_day3))
            self.label_27.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.day3max.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day3max.setText(str(round(res3[0][0]))+" °C")
            self.day3min.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day3min.setText(str(round(res3[1][0]))+" °C")
            self.day3humidity.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day3humidity.setText(str(round(t[2]))+" %")

#----------------------day 4 ke liye----------------------------
            t=newdf.loc[newdf["Date"].str.contains(d4)].mean()
            ma=round(t[0])
            mi=round(t[1])
            res4=predict(ma,mi)
            print(res4[0][0],res4[1][0])
            self.label_34.setText("Day 4:  "+str(label_day4))
            self.label_34.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.day4max.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day4max.setText(str(round(res4[0][0]))+" °C")
            self.day4min.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day4min.setText(str(round(res4[1][0]))+" °C")
            self.day4humidity.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day4humidity.setText(str(round(t[2]))+" %")
                         
#----------------------day 5 ke liye----------------------------
            t=newdf.loc[newdf["Date"].str.contains(d5)].mean()
            ma=round(t[0])
            mi=round(t[1])
            res5=predict(ma,mi)
            print(res5[0][0],res5[1][0])
            self.label_41.setText("Day 5:  "+str(label_day5))
            self.label_41.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.day5max.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day5max.setText(str(round(res5[0][0]))+" °C")
            self.day5min.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day5min.setText(str(round(res5[1][0]))+" °C")
            self.day5humidity.setStyleSheet("font: 500 9pt \"Segoe UI\";")
            self.day5humidity.setText(str(round(t[2]))+" %")


if __name__ == "__main__":
    import sys
    import pandas as pd 
    import numpy as np 
    import pandas as pd 
    import seaborn as sns 
    import matplotlib.pyplot as plt 
    from sklearn import preprocessing, svm 
    from sklearn.model_selection import train_test_split 
    from sklearn.linear_model import LinearRegression
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

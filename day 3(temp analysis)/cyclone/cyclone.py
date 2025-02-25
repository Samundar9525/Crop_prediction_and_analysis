# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cyclone.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn import preprocessing, svm 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 655)
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
        self.label_3.setGeometry(QtCore.QRect(10, 40, 131, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 180, 131, 220))
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
        self.frame_2.setGeometry(QtCore.QRect(150, 0, 671, 641))
        self.frame_2.setStyleSheet("background-color: rgb(0, 93, 93);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.templabel = QtWidgets.QLabel(self.frame_2)
        self.templabel.setGeometry(QtCore.QRect(230, 10, 251, 51))
        self.templabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 700 10pt \"Segoe UI\";")
        self.templabel.setObjectName("templabel")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(40, 140, 571, 61))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 291, 16))
        self.label_4.setObjectName("label_4")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(60, 30, 31, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(250, 30, 31, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(420, 30, 41, 16))
        self.label_16.setObjectName("label_16")
        self.jaipurmax = QtWidgets.QLabel(self.frame_4)
        self.jaipurmax.setGeometry(QtCore.QRect(100, 30, 71, 16))
        self.jaipurmax.setObjectName("jaipurmax")
        self.jaipurmin = QtWidgets.QLabel(self.frame_4)
        self.jaipurmin.setGeometry(QtCore.QRect(290, 30, 61, 16))
        self.jaipurmin.setObjectName("jaipurmin")
        self.jaipurwind = QtWidgets.QLabel(self.frame_4)
        self.jaipurwind.setGeometry(QtCore.QRect(470, 30, 80, 16))
        self.jaipurwind.setObjectName("jaipurwind")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(40, 210, 571, 61))
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 291, 16))
        self.label_5.setObjectName("label_5")
        self.label_17 = QtWidgets.QLabel(self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(60, 30, 31, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        self.label_18.setGeometry(QtCore.QRect(250, 30, 31, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(420, 30, 41, 16))
        self.label_19.setObjectName("label_19")
        self.mumbaimax = QtWidgets.QLabel(self.frame_5)
        self.mumbaimax.setGeometry(QtCore.QRect(100, 30, 61, 16))
        self.mumbaimax.setObjectName("mumbaimax")
        self.mumbaimin = QtWidgets.QLabel(self.frame_5)
        self.mumbaimin.setGeometry(QtCore.QRect(290, 30, 61, 16))
        self.mumbaimin.setObjectName("mumbaimin")
        self.mumbaiwind = QtWidgets.QLabel(self.frame_5)
        self.mumbaiwind.setGeometry(QtCore.QRect(470, 30, 61, 16))
        self.mumbaiwind.setObjectName("mumbaiwind")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(330, 290, 161, 41))
        self.label.setObjectName("label")
        self.windstatus = QtWidgets.QLabel(self.frame_2)
        self.windstatus.setGeometry(QtCore.QRect(500, 290, 150, 41))
        self.windstatus.setObjectName("windstatus")
        self.windspeed = QtWidgets.QLabel(self.frame_2)
        self.windspeed.setGeometry(QtCore.QRect(220, 290, 101, 41))
        self.windspeed.setObjectName("windspeed")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(40, 290, 151, 41))
        self.label_8.setObjectName("label_8")
        self.alert = QtWidgets.QLabel(self.frame_2)
        self.alert.setGeometry(QtCore.QRect(450, 390, 191, 131))
        self.alert.setText("")
        self.alert.setPixmap(QtGui.QPixmap(""))
        self.alert.setScaledContents(True)
        self.alert.setObjectName("alert")
        self.jaipurpredict = QtWidgets.QPushButton(self.frame_2)
        self.jaipurpredict.setGeometry(QtCore.QRect(40, 100, 201, 31))
        self.jaipurpredict.setStyleSheet("background-color: rgb(0, 130, 0);\n"
"font: 700 11pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.jaipurpredict.setObjectName("jaipurpredict")
        self.quotes = QtWidgets.QLabel(self.frame_2)
        self.quotes.setGeometry(QtCore.QRect(50, 400, 351, 81))
        self.quotes.setObjectName("quotes")
        self.test = QtWidgets.QPushButton(self.frame_2)
        self.test.setGeometry(QtCore.QRect(490, 100, 121, 31))
        self.test.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.test.setObjectName("test")
        self.mumbaipredict = QtWidgets.QPushButton(self.frame_2)
        self.mumbaipredict.setGeometry(QtCore.QRect(260, 100, 211, 31))
        self.mumbaipredict.setStyleSheet("background-color: rgb(0, 130, 0);\n"
"font: 700 11pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.mumbaipredict.setObjectName("mumbaipredict")
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
        self.templabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Cyclone Prediction</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">JAIPUR</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MAX</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MIN</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">WIND</span></p></body></html>"))
        self.jaipurmax.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.jaipurmin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.jaipurwind.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">MUMBAI</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MAX</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">MIN</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">WIND</span></p></body></html>"))
        self.mumbaimax.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.mumbaimin.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.mumbaiwind.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">00</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">WIND STATUS :</span></p></body></html>"))
        self.windstatus.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">NULL</span></p></body></html>"))
        self.windspeed.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">NULL</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">WIND SPEED :</span></p></body></html>"))
        self.jaipurpredict.setText(_translate("MainWindow", "Predict Jaipur Wind "))
        self.quotes.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\"></span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\"></span></p></body></html>"))
        self.test.setText(_translate("MainWindow", "Test"))
        self.mumbaipredict.setText(_translate("MainWindow", "Predict Mumbai Wind "))
        self.jaipurpredict.pressed.connect(self.jaipurfun)
        self.mumbaipredict.pressed.connect(self.mumbaifun)
        self.test.pressed.connect(self.testfun)        
    def jaipurfun(self):
            cols=list(df.columns)
            t=df[cols[0:1]]
            a=list(t["date_time"])
            b=[]
            c=[]
            for i in range(len(a)):
                    b.append(a[i][0:10])
                    c.append(a[i][12:17])   
            cols=list(df.columns)   
            newd=df[cols[1:7]]   
            tem1=pd.DataFrame(data=b,columns=["Date"]) 
            tem2=pd.DataFrame(data=c,columns=["time"]) 
            newdf=pd.concat([tem1,tem2,newd],axis=1)
            print(newdf.head())
            
            from datetime import date
            def dayfun(today):
                    res=""
                    if len(str(today.day))==1:
                            res='0'+str(today.day)+'-'
                    else:
                            res=str(today.day)+'-'

                    if len(str(today.month))==1:
                            res+='0'+str(today.month)
                    else:
                            res+=str(today.month)
                    return(res)

            inp=(dayfun(date.today()))
            t=newdf.loc[newdf["Date"].str.contains(inp+"-")]
            X=t.drop(["Date","time","mumwind","jaipurwind"],axis=1).values
            y=t["jaipurwind"].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,random_state=0)
            regr = LinearRegression()
            regr.fit(X_train, y_train) 
            print(regr.score(X_test, y_test))
            p=t.mean()
            inp_jaipurmax=round(p[0])
            inp_jaipurmin=round(p[1])
            inp_jaipurwind=round(p[2])
            inp_mumbaimax=round(p[3])
            inp_mumbaimin=round(p[4])
            inp_mumbaiwind=round(p[5])
            res=regr.predict([[inp_jaipurmax,inp_jaipurmin,inp_mumbaimax,inp_mumbaimin]])[0]
            print(res)
            self.jaipurmax.setText(str(inp_jaipurmax)+" °C")
            self.jaipurmax.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.jaipurmin.setText(str(inp_jaipurmin)+" °C")
            self.jaipurmin.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.jaipurwind.setText(str(inp_jaipurwind)+" km/h")
            self.jaipurwind.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.mumbaimax.setText(str(inp_mumbaimax)+" °C")
            self.mumbaimax.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.mumbaimin.setText(str(inp_mumbaimin)+" °C")
            self.mumbaimin.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.mumbaiwind.setText(str(inp_mumbaiwind)+" km/h")
            self.mumbaiwind.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            if (res)<15:
                    print("Normal Wind \t Speed : ",round(res))
                    self.windstatus.setText("Normal Wind")
                    self.windstatus.setStyleSheet("color:lightgreen;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:lightgreen;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/normalwind.png"))
                    self.quotes.setText("      Everything is fine \n       Have a Nice Day")
                    self.quotes.setStyleSheet("color:white;font: 900 16pt \"Segoe UI\";")
            elif (res)>15 and (res)<25:
                    print("heavy Wind \t Speed ",round(res))
                    self.windstatus.setText("Heavy Wind")
                    self.windstatus.setStyleSheet("color:tomato;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:tomato;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/normalwind.png"))
                    self.quotes.setText("       !!!! Be Alert !!!!!  \n       Have a Nice Day")
                    self.quotes.setStyleSheet("color:white;font: 900 16pt \"Segoe UI\";")
            else:
                    print("Cylone  \t Speed",round(res))
                    self.windstatus.setText("Cyclone")
                    self.windstatus.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/alert.png"))
                    self.quotes.setText("      !!!! Alert !!!!! \n Do not go Anywhere")
                    self.quotes.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
    def mumbaifun(self):
            cols=list(df.columns)
            t=df[cols[0:1]]
            a=list(t["date_time"])
            b=[]
            c=[]
            for i in range(len(a)):
                    b.append(a[i][0:10])
                    c.append(a[i][12:17])   
            cols=list(df.columns)   
            newd=df[cols[1:7]]   
            tem1=pd.DataFrame(data=b,columns=["Date"]) 
            tem2=pd.DataFrame(data=c,columns=["time"]) 
            newdf=pd.concat([tem1,tem2,newd],axis=1)
            print(newdf.head())
            
            from datetime import date
            def dayfun(today):
                    res=""
                    if len(str(today.day))==1:
                            res='0'+str(today.day)+'-'
                    else:
                            res=str(today.day)+'-'

                    if len(str(today.month))==1:
                            res+='0'+str(today.month)
                    else:
                            res+=str(today.month)
                    return(res)

            inp=(dayfun(date.today()))
            t=newdf.loc[newdf["Date"].str.contains(inp+"-")]
            X=t.drop(["Date","time","mumwind","jaipurwind"],axis=1).values
            y=t["mumwind"].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,random_state=0)
            regr = LinearRegression()
            regr.fit(X_train, y_train) 
            print(regr.score(X_test, y_test))
            p=t.mean()
            inp_jaipurmax=round(p[0])
            inp_jaipurmin=round(p[1])
            inp_jaipurwind=round(p[2])
            inp_mumbaimax=round(p[3])
            inp_mumbaimin=round(p[4])
            inp_mumbaiwind=round(p[5])

            res=regr.predict([[inp_jaipurmax,inp_jaipurmin,inp_mumbaimax,inp_mumbaimin]])[0]
            print(res)

            self.jaipurmax.setText(str(inp_jaipurmax)+" °C")
            self.jaipurmax.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.jaipurmin.setText(str(inp_jaipurmin)+" °C")
            self.jaipurmin.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.jaipurwind.setText(str(inp_jaipurwind)+" km/h")
            self.jaipurwind.setStyleSheet("font: 700 9pt \"Segoe UI\";")

            self.mumbaimax.setText(str(inp_mumbaimax)+" °C")
            self.mumbaimax.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.mumbaimin.setText(str(inp_mumbaimin)+" °C")
            self.mumbaimin.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.mumbaiwind.setText(str(inp_mumbaiwind)+" km/h")
            self.mumbaiwind.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            if (res)<15:
                    print("Normal Wind \t Speed : ",round(res))
                    self.windstatus.setText("Normal Wind")
                    self.windstatus.setStyleSheet("color:lightgreen;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:lightgreen;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/normalwind.png"))
                    self.quotes.setText("      Everything is fine \n       Have a Nice Day")
                    self.quotes.setStyleSheet("color:white;font: 900 16pt \"Segoe UI\";")
            elif (res)>15 and (res)<25:
                    print("heavy Wind \t Speed ",round(res))
                    self.windstatus.setText("Heavy Wind")
                    self.windstatus.setStyleSheet("color:tomato;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:tomato;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/normalwind.png"))
                    self.quotes.setText("       !!!! Be Alert !!!!!  \n       Have a Nice Day")
                    self.quotes.setStyleSheet("color:white;font: 900 16pt \"Segoe UI\";")
            else:
                    print("Cylone  \t Speed",round(res))
                    self.windstatus.setText("Cyclone")
                    self.windstatus.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/alert.png"))
                    self.quotes.setText("      !!!! Alert !!!!! \n Do not go Anywhere")
                    self.quotes.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
    def testfun(self):
            cols=list(df.columns)
            t=df[cols[0:1]]
            a=list(t["date_time"])
            b=[]
            c=[]
            for i in range(len(a)):
                    b.append(a[i][0:10])
                    c.append(a[i][12:17])   
            cols=list(df.columns)   
            newd=df[cols[1:7]]   
            tem1=pd.DataFrame(data=b,columns=["Date"]) 
            tem2=pd.DataFrame(data=c,columns=["time"]) 
            newdf=pd.concat([tem1,tem2,newd],axis=1)
            print(newdf.head())
            
            from datetime import date
            def dayfun(today):
                    res=""
                    if len(str(today.day))==1:
                            res='0'+str(today.day)+'-'
                    else:
                            res=str(today.day)+'-'

                    if len(str(today.month))==1:
                            res+='0'+str(today.month)
                    else:
                            res+=str(today.month)
                    return(res)

        #     inp=(dayfun(date.today()))
            inp="08-08"
            t=newdf.loc[newdf["Date"].str.contains(inp+"-")]
            X=t.drop(["Date","time","mumwind","jaipurwind"],axis=1).values
            y=t["mumwind"].values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,random_state=0)
            regr = LinearRegression()
            regr.fit(X_train, y_train) 
            print(regr.score(X_test, y_test))
            p=t.mean()
            inp_jaipurmax=38
            inp_jaipurmin=19
            inp_jaipurwind=round(p[2])
            inp_mumbaimax=18
            inp_mumbaimin=22
            inp_mumbaiwind=round(p[5])
            res=regr.predict([[inp_jaipurmax,inp_jaipurmin,inp_mumbaimax,inp_mumbaimin]])[0]
            print(res)
            self.jaipurmax.setText(str(inp_jaipurmax)+" °C")
            self.jaipurmax.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.jaipurmin.setText(str(inp_jaipurmin)+" °C")
            self.jaipurmin.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.jaipurwind.setText(str(inp_jaipurwind)+" km/h")
            self.jaipurwind.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.mumbaimax.setText(str(inp_mumbaimax)+" °C")
            self.mumbaimax.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.mumbaimin.setText(str(inp_mumbaimin)+" °C")
            self.mumbaimin.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            self.mumbaiwind.setText(str(inp_mumbaiwind)+" km/h")
            self.mumbaiwind.setStyleSheet("font: 700 9pt \"Segoe UI\";")
            if (res)<15:
                    print("Normal Wind \t Speed : ",round(res))
                    self.windstatus.setText("Normal Wind")
                    self.windstatus.setStyleSheet("color:lightgreen;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:lightgreen;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/normalwind.png"))
            elif (res)>15 and (res)<25:
                    print("heavy Wind \t Speed ",round(res))
                    self.windstatus.setText("Heavy Wind")
                    self.windstatus.setStyleSheet("color:tomato;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:tomato;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/normalwind.png"))
            else:
                    print("Cylone  \t Speed",round(res))
                    self.windstatus.setText("Cyclone")
                    self.windstatus.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
                    self.windspeed.setText(str(round(res))+" km/hr")
                    self.windspeed.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
                    self.alert.setPixmap(QtGui.QPixmap("image/alert.png"))
                    self.quotes.setText("      !!!! Alert !!!!! \n Do not go Anywhere")
                    self.quotes.setStyleSheet("color:red;font: 900 16pt \"Segoe UI\";")
if __name__ == "__main__":
    import sys
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    df=pd.read_csv("sam.csv")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Update(object):
    def setupUi(self, Update):
        Update.setObjectName("Update")
        Update.resize(700, 399)
        Update.setMinimumSize(QtCore.QSize(700, 399))
        Update.setMaximumSize(QtCore.QSize(700, 399))
        Update.setStyleSheet("background-color: rgb(235, 255, 190)")
        self.centralwidget = QtWidgets.QWidget(Update)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_17.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_17.setSpacing(9)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(150, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(110, 40))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"  background-color:rgb(255, 195, 125);\n"
"  color: black;\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(188, 143, 92), stop: 1 #ffc37d );\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(227, 173, 111), stop: 1 #ffc37d);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(110, 40))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"  background-color:rgb(255, 195, 125);\n"
"  color: black;\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(188, 143, 92), stop: 1 #ffc37d );\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(227, 173, 111), stop: 1 #ffc37d);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(110, 40))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"  background-color:rgb(255, 195, 125);\n"
"  color: black;\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(188, 143, 92), stop: 1 #ffc37d );\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 rgb(227, 173, 111), stop: 1 #ffc37d);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_17.addLayout(self.horizontalLayout)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("font-size:30px;\n"
"text-transform: uppercase;\n"
"font-weight: 100;\n"
"  background-color:rgb(255, 195, 125);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("font-size: 24px;\n"
"font-weight: bold;\n"
"color: #222;\n"
"qproperty-alignment: AlignCenter;")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("font-size: 14px;\n"
"color: #222;\n"
"")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setStyleSheet("font-weight: 700;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: #8080FF;\n"
"qproperty-alignment: AlignCenter;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_3.setStyleSheet("font-size: 10px;\n"
"color: #222;\n"
"font-weight: 700;\n"
"qproperty-alignment: AlignCenter;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font-size: 13px;\n"
"color: #222;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(60, 0))
        self.label_4.setStyleSheet("font-weight: 700;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: red;\n"
"qproperty-alignment: AlignCenter;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_5.setStyleSheet("font-size: 10px;\n"
"color: #222;\n"
"font-weight: 700;\n"
"qproperty-alignment: AlignCenter;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font-size: 13px;\n"
"color: #222;\n"
"")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setStyleSheet("font-size:30px;\n"
"text-transform: uppercase;\n"
"font-weight: 100;\n"
"  background-color:rgb(255, 195, 125);")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_11.addWidget(self.label_20)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem4)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setStyleSheet("font-size: 24px;\n"
"font-weight: bold;\n"
"color: #222;\n"
"qproperty-alignment: AlignCenter;")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_13.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setStyleSheet("font-size: 14px;\n"
"color: #222;\n"
"\n"
"")
        self.label_22.setObjectName("label_22")
        self.verticalLayout_13.addWidget(self.label_22)
        self.verticalLayout_12.addLayout(self.verticalLayout_13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setMinimumSize(QtCore.QSize(60, 0))
        self.label_23.setStyleSheet("font-weight: 700;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color: #8ACA2B;\n"
"qproperty-alignment: AlignCenter;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_9.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_24.setStyleSheet("font-size: 10px;\n"
"color: #222;\n"
"font-weight: 700;\n"
"qproperty-alignment: AlignCenter;")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_9.addWidget(self.label_24)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setStyleSheet("font-size: 13px;\n"
"color: #222;")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_14.addWidget(self.label_25)
        self.horizontalLayout_8.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setMinimumSize(QtCore.QSize(60, 0))
        self.label_26.setStyleSheet("font-weight: 700;\n"
"font-size: 20px;\n"
"font-weight: bold;\n"
"color:#222;\n"
"qproperty-alignment: AlignCenter;")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_10.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_27.setStyleSheet("font-size: 10px;\n"
"color: #222;\n"
"font-weight: 700;\n"
"qproperty-alignment: AlignCenter;")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_10.addWidget(self.label_27)
        self.verticalLayout_15.addLayout(self.horizontalLayout_10)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setStyleSheet("font-size: 13px;\n"
"color: #222;\n"
"")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_15.addWidget(self.label_28)
        self.horizontalLayout_8.addLayout(self.verticalLayout_15)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_16.addLayout(self.horizontalLayout_11)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem5)
        self.verticalLayout_17.addLayout(self.verticalLayout_16)
        Update.setCentralWidget(self.centralwidget)

        self.retranslateUi(Update)
        QtCore.QMetaObject.connectSlotsByName(Update)

    def retranslateUi(self, Update):
        _translate = QtCore.QCoreApplication.translate
        Update.setWindowTitle(_translate("Update", "MainWindow"))
        self.label.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#4c611f;\">CVOID-19</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Update", "Updates"))
        self.pushButton_9.setText(_translate("Update", "Countries"))
        self.pushButton_2.setText(_translate("Update", "Graphs"))
        self.label_10.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Active Cases</span></p></body></html>"))
        self.label_8.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Test</span></p></body></html>"))
        self.label_9.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Currently Infected Patients</span></p></body></html>"))
        self.label_2.setText(_translate("Update", "<html><head/><body><p><span style=\" font-size:15pt;\">Test</span></p></body></html>"))
        self.label_3.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">(T)</span></p></body></html>"))
        self.label_6.setText(_translate("Update", "<html><head/><body><p align=\"center\">in Mid Condition</p></body></html>"))
        self.label_4.setText(_translate("Update", "<html><head/><body><p><span style=\" font-size:15pt;\">Test</span></p></body></html>"))
        self.label_5.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">(T)</span></p></body></html>"))
        self.label_7.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Serious or Critical</span></p></body></html>"))
        self.label_20.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Closed Cases</span></p></body></html>"))
        self.label_21.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Test</span></p></body></html>"))
        self.label_22.setText(_translate("Update", "<html><head/><body><p align=\"center\">Cases which had an outcome:</p></body></html>"))
        self.label_23.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Test</span></p></body></html>"))
        self.label_24.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">(T)</span></p></body></html>"))
        self.label_25.setText(_translate("Update", "<html><head/><body><p align=\"center\">Recovered</p></body></html>"))
        self.label_26.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt;\">Test</span></p></body></html>"))
        self.label_27.setText(_translate("Update", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">(T)</span></p></body></html>"))
        self.label_28.setText(_translate("Update", "<html><head/><body><p align=\"center\">Deaths</p></body></html>"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
from plot import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 311)
        MainWindow.setWindowIcon(QIcon("icon.ico"))
        MainWindow.setMaximumSize(QtCore.QSize(380, 311))
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: #00838f;\n"
"}\n"
"QLabel{\n"
"font: 14pt \"Roboto\";\n"
"color: white;\n"
"}\n"
"QPushButton{\n"
"font: 14pt \"Roboto\";\n"
"border: 0px;\n"
"background-color: rgb(0, 230, 0);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton:open{\n"
"background-color: rgb(0, 255, 0);\n"
"}\n"
"QLineEdit{\n"
"border: 0px;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 0, 221, 51))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 210, 331, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 231, 31))
        self.label_3.setObjectName("label_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 110, 331, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openFileNameDialog)
        self.pushButton_2.clicked.connect(self.graph_plot)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IRG_ORCA"))
        self.label.setText(_translate("MainWindow", "Graph Infrared Spectrum "))
        self.pushButton_2.setText(_translate("MainWindow", "Plot"))
        self.label_2.setText(_translate("MainWindow", "1.- Open file .dat "))
        self.label_3.setText(_translate("MainWindow", "2.- Click on graphics"))
        self.pushButton.setText(_translate("MainWindow", "Open"))

    def openFileNameDialog(self):
        fileName = QFileDialog.getOpenFileName(None, 'Open file ORCA .dat', "", "ORCA *.dat")
        self.lineEdit.setText(fileName[0])        
			
    def graph_plot(self):
	    if (self.lineEdit.text() != '' ):
	        plot_IR(self.lineEdit.text())
        #pass
            
			
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *

import Database

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(620, 340)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("register.jpg")))
        MainWindow.setPalette(palette)
        MainWindow.setObjectName("TQ")
        MainWindow.activateWindow()
        MainWindow.setWindowIcon(QIcon('coffee.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 201, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 201, 51))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 29, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 80, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 130, 191, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 201, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 180, 201, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dbu = Database.DatabaseUtility()
        self.pushButton.clicked.connect(self.checkerror)
        self.pushButton_2.clicked.connect(self.create)
        self.flag=0
        self.flag1=0
        self.flag2=0
        self.run=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;color:#DAA520\">NAME : </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;color:#DAA520\">PHONE NO :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;color:#DAA520\">CLG ID :</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "CHECK VALIDITY"))
        self.pushButton_2.setText(_translate("MainWindow", "CREATE ACCOUNT"))
    def create(self):
        if self.flag1==1 and self.flag2==1 or self.run==0:
            self.error= QtWidgets.QMessageBox()
            self.error.setText("PLEASE CHECK VALIDITY AND THEN PROCEED.")
            self.error.setWindowTitle("ERROR")
            self.error.show()
        else:
            self.text1=self.lineEdit.text().upper()
            self.text2=self.lineEdit_2.text().upper()
            self.text3 = self.lineEdit_3.text().upper()
            self.dbu.create_table(self.text1,self.text2,self.text3)
            self.dbu.disconnect()
            self.created = QtWidgets.QMessageBox()
            self.created.setText("ACCOUNT CREATED.\nTHE CARD NO IS CU"+self.text3)
            self.created.setWindowTitle("CONGRATS")
            self.created.show()
        self.run=0
    def checkerror(self):
        self.run=1
        self.flag=0
        self.flag2=0
        self.count=0
        text=self.lineEdit.text()
        for char in text:
            if char.isdigit():
                self.flag=1
        length=len(text)
        text1 = self.lineEdit_2.text()
        text1.upper()
        length1=len(text1)
        text2 = self.lineEdit_3.text()
        text2.upper()
        length2=len(text2)
        self.flag2= self.dbu.check_validity(text2)
        if length==0 or self.flag==1:
            self.error = QtWidgets.QMessageBox()
            self.error.setText("PLEASE ENTER THE NAME IN CORRECT FORMAT.\nCONSTRAINT:\nTHE NAME SHOULD NOT CONTAIN A NUMBER")
            self.error.setWindowTitle("ERROR")
            self.error.show()
        if length1 == 0:
            self.error1 = QtWidgets.QMessageBox()
            self.error1.setText("PLEASE ENTER THE PHONE NO.")
            self.error1.setWindowTitle("ERROR")
            self.error1.show()
        if length2 == 0 :
            self.error2 = QtWidgets.QMessageBox()
            self.error2.setText("PLEASE ENTER THE CARD NO.")
            self.error2.setWindowTitle("ERROR")
            self.error2.show()
        if self.flag2==1:
            self.error3 = QtWidgets.QMessageBox()
            self.error3.setText("THE CARD NO ALREADY EXISTS.")
            self.error3.setWindowTitle("ERROR")
            self.error3.show()
        if self.count==0:
            self.err = QtWidgets.QMessageBox()
            self.err.setText("PROCEED TO CREATE ACCOUNT.")
            self.err.setWindowTitle("ERROR")
            self.err.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


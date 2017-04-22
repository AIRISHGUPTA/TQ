from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("background1.jpg")))
        MainWindow.setPalette(palette)
        MainWindow.setObjectName("TQ")
        MainWindow.resize(516, 282)
        MainWindow.activateWindow()
        MainWindow.setWindowIcon(QIcon('coffee.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 101, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 141, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 121, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150,140, 152, 30))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 70, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 120, 141, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 120, 151, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.create)
        self.pushButton_2.clicked.connect(self.checkerror)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("NEW REGISTRATION", "NEW REGISTRATION"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">NAME :</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">PHONE NO :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">CARD NO :</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "CREATE "))
        self.pushButton_2.setText(_translate("MainWindow", "CHECK CARD NO VALIDITY"))

    def create(self,MainWindow):
        import Database
        self.text1=self.lineEdit.text()
        self.text2=self.lineEdit_2.text()
        self.text3 = self.lineEdit_3.text()
        self.text1.upper()
        self.text2.upper()
        self.text3.upper()
        create=Database.DatabaseUtility('register')
        create.create_table(self.text1,self.text2,self.text3)
        create.disconnect()
        MainWindow.close()
        self.label_2.set

    def checkerror(self):
        text = self.lineEdit_3.text()
        text.upper()
        length=len(text)
        import Database
        check=Database.DatabaseUtility('register')
        ans= check.check_validity(text)
        if (ans==1 and length>0):
            _translate = QtCore.QCoreApplication.translate
            self.label_4.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:18pt;\">NOT VALID</span></p></body></html>"))
        if (ans==0 and length>0):
            _translate = QtCore.QCoreApplication.translate
            self.label_4.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:18pt;\">VALID</span></p></body></html>"))



def main():

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()
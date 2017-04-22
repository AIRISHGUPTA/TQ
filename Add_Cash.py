from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
class Ui_MainWindow2(object):
    def setupUi(self, MainWindow,cardno):
        self.cardno=cardno
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 200)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("cash.jpg")))
        MainWindow.setPalette(palette)
        MainWindow.setWindowIcon(QIcon('coffee.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 51))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 20, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(134, 110, 141, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.add_cash)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#550000;\">ENTER AMMOUNT :</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "ADD CASH "))
    def add_cash(self):
        import Database
        self.text=self.lineEdit.text().upper()
        self.dbu=Database.DatabaseUtility()
        self.dbu.add_cash(self.text,self.cardno)
        self.dbu.disconnect()
        self.prompt = QtWidgets.QMessageBox()
        self.prompt.setText("CASH ADDED SUCCESSFULLY.      ")
        self.prompt.setWindowTitle("CASH STATUS")
        self.prompt.setWindowIcon(QIcon('coffee.jpg'))
        self.prompt.show()


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("back.jpg")))
        MainWindow.setPalette(palette)
        MainWindow.showFullScreen()
        MainWindow.setWindowIcon(QIcon('coffee.jpg'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 551, 81))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 261, 71))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 120, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(910, 170, 401, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(910, 220, 411, 41))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 170, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 170, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 120, 75, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 120, 75, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(910, 280, 411, 361))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1341, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_3.clicked.connect(self.add_cash)
        self.pushButton_4.clicked.connect(self.display)
        self.pushButton_2.clicked.connect(self.open_app)
        self.pushButton.clicked.connect(self.order)
        self.treeWidget.setColumnCount(2)
        columns = ['TIMIMGS', 'BILL']
        self.treeWidget.setHeaderLabels(columns)
        self.treeWidget.setWindowOpacity(0.5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#aa0000;\">WELCOME TO TQ</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#DAA520;\">ENTER CARD NO :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#DAA520;\">NAME :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#DAA520;\">CASH AVAILABLE :</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "ORDER"))
        self.pushButton_2.setText(_translate("MainWindow", "NEW REGISTRATION"))
        self.pushButton_3.setText(_translate("MainWindow", "ADD CASH"))
        self.pushButton_4.setText(_translate("MainWindow", "STATUS"))

    def display(self):
        import Database
        ans=0
        flag=0
        self.cardno = self.lineEdit.text().upper()
        print(self.cardno)
        length=len(self.cardno)
        self.dbu = Database.DatabaseUtility()
        ans = self.dbu.get_name(self.cardno)

        if (not ans) and self.cardno!="REGISTER" or length==0:
            self.invalid = QtWidgets.QMessageBox()
            self.invalid.setText("INVALID CARD NO.      ")
            self.invalid.setWindowTitle("ERROR")
            self.invalid.setWindowIcon(QIcon('coffee.jpg'))
            self.invalid.show()
        if ans and self.cardno!="REGISTER":
            name = 'NAME : ' + ans[0][0]
            word="CASH AVAILABLE : "+ans[0][1]

            self.label_3.setText(name)
            self.label_3.setStyleSheet("font-size:18pt; color:#DAA520")
            self.label_4.setText(word)
            self.label_4.setStyleSheet("font-size:18pt; color:#DAA520")
            flag = 1
        if flag == 1:
            self.treeWidget.setColumnCount(2)
            columns = ['TIMIMGS', 'BILL']
            self.treeWidget.setHeaderLabels(columns)
            self.treeWidget.clear()
            table = self.dbu.get_table(self.cardno)
            l = []
            for i in table:
                l.append(QtWidgets.QTreeWidgetItem(i))
            self.treeWidget.addTopLevelItems(l)

        if self.cardno == 'REGISTER':
            self.treeWidget.setColumnCount(4)
            columns = ['NAME', 'PHONE NO', 'CARDNO', 'BALANCE']
            self.treeWidget.setHeaderLabels(columns)
            self.treeWidget.clear()
            table = self.dbu.get_register()
            l = []
            for i in table:
                l.append(QtWidgets.QTreeWidgetItem(i))
            self.treeWidget.addTopLevelItems(l)
        self.dbu.disconnect()
    def add_cash(self):
        import Database
        ans=1
        self.cardno = self.lineEdit.text().upper()
        length = len(self.cardno)
        self.dbu = Database.DatabaseUtility()
        ans = self.dbu.get_name(self.cardno)
        print(ans)
        print((not ans) and self.cardno != "REGISTER" or length == 0)
        if ((not ans) or length == 0) :
            from PyQt5 import QtCore, QtGui, QtWidgets
            self.invalid = QtWidgets.QMessageBox()
            self.invalid.setText("INVALID CARD NO.      ")
            self.invalid.setWindowTitle("ERROR")
            self.invalid.setWindowIcon(QIcon('coffee.jpg'))
            self.invalid.show()
        else:
            import Add_Cash
            from PyQt5 import QtCore, QtGui, QtWidgets
            self.Window = QtWidgets.QMainWindow()
            self.ui = Add_Cash.Ui_MainWindow2()
            self.ui.setupUi(self.Window, self.cardno)
            self.Window.show()
        self.dbu.disconnect()
    def order(self):
        import Database
        ans = 1
        self.cardno = self.lineEdit.text().upper()
        length = len(self.cardno)
        self.dbu = Database.DatabaseUtility()
        ans = self.dbu.get_name(self.cardno)
        print(ans)
        print((not ans) and self.cardno != "REGISTER" or length == 0)
        if ((not ans) or length == 0):
            from PyQt5 import QtCore, QtGui, QtWidgets
            self.invalid = QtWidgets.QMessageBox()
            self.invalid.setText("INVALID CARD NO.      ")
            self.invalid.setWindowTitle("ERROR")
            self.invalid.setWindowIcon(QIcon('coffee.jpg'))
            self.invalid.show()
        else:
            self.cardno=self.lineEdit.text().upper()
            import ORDER
            from PyQt5 import QtCore, QtGui, QtWidgets
            self.Window = QtWidgets.QMainWindow()
            self.ui = ORDER.Ui_MainWindow3()
            self.ui.setupUi(self.Window,self.cardno)
            self.Window.show()

    def open_app(self):
        import New_Member
        from PyQt5 import QtCore, QtGui, QtWidgets
        self.Window = QtWidgets.QMainWindow()
        self.ui = New_Member.Ui_MainWindow1()
        self.ui.setupUi(self.Window)
        self.Window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


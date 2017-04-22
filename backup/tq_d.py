# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tq_design.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("background2.png")))
        MainWindow.setPalette(palette)
        MainWindow.showMaximized()
        MainWindow.setWindowIcon(QIcon('coffee.jpg'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 421, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 241, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 120, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 160, 75, 23))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 90, 161, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 160, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 220, 421, 441))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 220, 631, 521))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1340, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.display)
        self.pushButton_3.clicked.connect(self.open_app)
        self.treeWidget.setColumnCount(2)
        columns = ['TIMIMGS','BILL']
        self.treeWidget.setHeaderLabels(columns)
        self.treeWidget.setWindowOpacity(0.5)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TQ", "TQ"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#b90000;\">WELCOME TO TQ</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; color:#aaaa00;\">ENTER CARD NO :</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "STATUS"))
        self.pushButton_2.setText(_translate("MainWindow", "ORDER"))
        self.pushButton_3.setText(_translate("MainWindow", "NEW REGISTRATON"))
        self.pushButton_4.setText(_translate("MainWindow", "ADD MONEY"))


    def display(self):
        import Database
        self.tbname = self.lineEdit.text()
        length=len(self.tbname)

        self.dbu = Database.DatabaseUtility(self.tbname)
        self.treeWidget.clear()
        table = self.dbu.get_table()
        l = []
        for i in table:
            l.append(QtWidgets.QTreeWidgetItem(i))
        self.treeWidget.addTopLevelItems(l)
        self.dbu.disconnect()
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


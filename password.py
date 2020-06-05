#3/6/20
#PyQt5 password Generator
#Created by 00MB

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 520)
        MainWindow.setMinimumSize(QtCore.QSize(770, 520))
        MainWindow.setMaximumSize(QtCore.QSize(770, 520))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #GenerateButton
        self.GenerateButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateButton.setGeometry(QtCore.QRect(260, 230, 221, 81))
        self.GenerateButton.setMaximumSize(QtCore.QSize(1677, 1677))
        self.GenerateButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.GenerateButton.setObjectName("GenerateButton")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.GenerateButton.setFont(font)
        self.GenerateButton.setStyleSheet("background-color: red;")
        self.GenerateButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.GenerateButton.clicked.connect(self.buttonClicked)

        #PasswordDisplay
        self.PasswordDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.PasswordDisplay.setGeometry(QtCore.QRect(30, 340, 701, 131))
        self.PasswordDisplay.setObjectName("PasswordDisplay")
        self.PasswordDisplay.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.PasswordDisplay.setFont(font)
        self.PasswordDisplay.setStyleSheet('background-color: grey; color: white;')

        #LengthFrame
        self.LengthFrame = QtWidgets.QFrame(self.centralwidget)
        self.LengthFrame.setGeometry(QtCore.QRect(30, 40, 291, 171))
        self.LengthFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LengthFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LengthFrame.setObjectName("LengthFrame")
        self.LengthFrame.setStyleSheet('background-color:grey; border-radius:25px;')

        #LengthLabel
        self.LengthLabel = QtWidgets.QLabel(self.LengthFrame)
        self.LengthLabel.setGeometry(QtCore.QRect(10, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LengthLabel.setFont(font)
        self.LengthLabel.setObjectName("LengthLabel")

        #LengthInput
        self.LengthInput = QtWidgets.QSpinBox(self.LengthFrame)
        self.LengthInput.setGeometry(QtCore.QRect(10, 60, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LengthInput.setFont(font)
        self.LengthInput.setObjectName("LengthInput")
        self.LengthInput.setStyleSheet('background-color: #c9c8c3;border-radius:0px;')
        self.LengthInput.setRange(8,30)

        #SymbolNumberFrame
        self.SymNumFrame = QtWidgets.QFrame(self.centralwidget)
        self.SymNumFrame.setGeometry(QtCore.QRect(400, 40, 331, 171))
        self.SymNumFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SymNumFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SymNumFrame.setObjectName("SymNumFrame")
        self.SymNumFrame.setStyleSheet('background-color:grey; border-radius:25px;')

        #SymbolLabel
        self.SymbolsLabel = QtWidgets.QLabel(self.SymNumFrame)
        self.SymbolsLabel.setGeometry(QtCore.QRect(20, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SymbolsLabel.setFont(font)
        self.SymbolsLabel.setObjectName("SymbolsLabel")

        #NumbersLabel
        self.NumbersLabel = QtWidgets.QLabel(self.SymNumFrame)
        self.NumbersLabel.setGeometry(QtCore.QRect(20, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.NumbersLabel.setFont(font)
        self.NumbersLabel.setObjectName("NumbersLabel")

        #NumbersBox
        self.NumbersBox = QtWidgets.QCheckBox(self.SymNumFrame)
        self.NumbersBox.setGeometry(QtCore.QRect(270, 100, 31, 31))
        self.NumbersBox.setText("")
        self.NumbersBox.setIconSize(QtCore.QSize(50, 50))
        self.NumbersBox.setChecked(False)
        self.NumbersBox.setObjectName("NumbersBox")
        self.NumbersBox.setStyleSheet("QCheckBox::indicator { width: 30px; height: 30px;}")

        #SymbolsBox
        self.SymbolsBox = QtWidgets.QCheckBox(self.SymNumFrame)
        self.SymbolsBox.setGeometry(QtCore.QRect(270, 20, 31, 31))
        self.SymbolsBox.setText("")
        self.SymbolsBox.setIconSize(QtCore.QSize(50, 50))
        self.SymbolsBox.setChecked(False)
        self.SymbolsBox.setObjectName("SymbolsBox")
        self.SymbolsBox.setStyleSheet("QCheckBox::indicator { width: 30px; height: 30px;}")

        #MenuBar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setStyleSheet("background-color: #303030;")
        MainWindow.setWindowTitle("Secure Password Generator")
        self.GenerateButton.setText(_translate("MainWindow", "Generate"))
        self.LengthLabel.setText(_translate("MainWindow", "Length of Password:"))
        self.SymbolsLabel.setText(_translate("MainWindow", "Include Symbols:"))
        self.NumbersLabel.setText(_translate("MainWindow", "Include Numbers:"))

    def checkNumbers(self):
        if self.NumbersBox.isChecked():
            return True
        return False

    def buttonClicked(self):
        chars = "hijklmnoABCDEFG"
        nums = "0123456789"
        sym = "?!£$%&"
        self.GenerateButton.setStyleSheet("background-color: blue;")
        if self.NumbersBox.isChecked() and "0" not in chars:
            chars += nums
        if self.SymbolsBox.isChecked() and "?" not in chars:
            chars += sym
        if self.NumbersBox.isChecked() and self.NumbersBox.isChecked() and "0" not in chars and "?" not in chars:
            chars = nums + sym
        Password = ''.join(random.choice(chars) for x in range(self.LengthInput.value()))
        self.PasswordDisplay.setText(Password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

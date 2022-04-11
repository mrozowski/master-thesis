from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtGui


class Bulb(QLabel):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(x, y, 45, 45))
        self.setScaledContents(True)
        self.setOff()

    def setOn(self):
        self.setPixmap(QtGui.QPixmap("graphic/bulb_on.png"))

    def setOff(self):
        self.setPixmap(QtGui.QPixmap("graphic/bulb_off.png"))

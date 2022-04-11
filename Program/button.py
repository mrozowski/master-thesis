from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRectF, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QAbstractButton
from config import TEXT_COLOR_DARK as dark_text, GRAY_ACCENT as disabled_font


class MenuButton(QAbstractButton):
    """Custom buttons"""

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.text = text
        self.pixmap = QtGui.QPixmap("graphic/button_menu.png")
        self.pixmap_hover = QtGui.QPixmap("graphic/button_menu_hover.png")
        self.pixmap_pressed = QtGui.QPixmap("graphic/button_menu_clicked.png")
        self.setStyleSheet("color: " + dark_text + ";")
        self.setFont(getFont(12))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def paintEvent(self, event):
        """show the button"""
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pix)
        painter.drawText(QRectF(0, -1, self.width(), self.height()), Qt.AlignCenter, self.text)

    def setDisabled(self, a0: bool) -> None:
        super(MenuButton, self).setDisabled(a0)
        if a0:
            self.setStyleSheet("color: " + disabled_font + ";")
        else:
            self.setStyleSheet("color: " + dark_text + ";")


def getFont(size):
    font = QtGui.QFont()
    font.setPointSize(size)
    return font

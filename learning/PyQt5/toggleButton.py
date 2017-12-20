#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
    QFrame)
from PyQt5.QtGui import QColor

class Toggle(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        grnb = QPushButton('Green', self)
        grnb.setCheckable(True)
        grnb.move(10, 60)

        grnb.clicked[bool].connect(self.setColor)

        self.squeare = QFrame(self)
        self.squeare.setGeometry(150, 20, 100, 100)
        self.squeare.setStyleSheet('QWidget { background-color: %s }' %
            self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle Button')
        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.col.setRed(val)
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.squeare.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    a = Toggle()
    sys.exit(app.exec_())

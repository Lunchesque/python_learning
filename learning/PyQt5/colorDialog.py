#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

class ColorDialog(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        col = QColor(1, 1, 1)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }'
            %col.name())
        self.frm.setGeometry(180, 20, 50, 50)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Color Dialog')
        self.show()

    def showDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }'
                %col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ColorDialog()
    sys.exit(app.exec_())

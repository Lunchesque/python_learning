#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Escape(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250,250)
        self.setWindowTitle('Реимплеминтация')
        self.show()

    def keyPressEvent(self, q):

        if q.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Escape()
    sys.exit(app.exec_())

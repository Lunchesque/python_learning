#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QObject

#создан новый сигнал closeApp, этот сигнал тригерится mousePressEvent

class Communicate(QObject):

    #сигнал closeApp сознан атрибутом pyqtSignal() внешнего класса Communicate
    closeApp = pyqtSignal()

class Emit(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close)     #соединение сигнала closeApp со слотом close() от QMainWindow

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Emiting Signal')
        self.show()

    def mousePressEvent(self, event):

        #при нажатии на окно указателем мыши сигнал closeApp "излучается" и приложение закрывается
        self.c.closeApp.emit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Emit()
    sys.exit(app.exec_())

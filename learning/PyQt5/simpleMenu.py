#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class SimpleMenu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')   #при описании шорткатов между между кнопками пробелов не должно быть
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&exitApp')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Simple_Menu')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = SimpleMenu()
    sys.exit(app.exec_())

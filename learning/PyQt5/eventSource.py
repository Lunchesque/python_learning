#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *

class Source(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #создание кнопок
        btn1 = QPushButton('Button 1', self)
        btn1.move(30,50)

        btn2 = QPushButton('Button 2', self)
        btn2.move(150, 50)

        #использование структуры сигнал-слот: сигнал - нажатие кнопки ".clicked", слот(приемник) - метод "buttonCliched"
        #при приеме сигнала слотом запускается метод слота и происходит реакция на сигнал
        #таким образом можно определить при необходимости источник сигнала для отлова ошибок
        btn1.clicked.connect(self.buttonCliched)
        btn2.clicked.connect(self.buttonCliched)

        self.statusBar()

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Event Source')
        self.show()

        #в этом методе узнается какая кнопка была нажата(это слот), метод sender() посылает иформацию в указанное место,ъ
        #в этом случае в statusBar, таким образом можно узнать источник сигнала, не только нажатия кнопки но и всего остального
    def buttonCliched(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Source()
    sys.exit(app.exec_())

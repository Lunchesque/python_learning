#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Obj(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = 'x: {0}, y: {1}'.format(x, y)   #в текстовом формате вывод значений координат мыши в QLabel виджете

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        #трекер мыши отключен по умолчанию, если оставить его выключенным, то будут выводится координаты последней
        #нажатой кнопки, когда setMouseTracking принимает значение True виджет принимает события движения мыши
        #даже если ни одной кнопки мыше не нажимать
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Event obj')
        self.show()


        #"e" - объект события, он содержит информацию о затригереном событии(в этом случае - движение мыши)
        #методами x(), y() определяютя координаты указателя мыши, создается строка и передается в основной виджет
    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Obj()
    sys.exit(app.exec_())

#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class SigSlot(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)      #создание lcd дисплея
        sld = QSlider(Qt.Horizontal, self)  #создание горизонтального слайдера

        vbox = QVBoxLayout()    #разметка окна приложения (каждый элемент находится друг под другом, как в отдельном прямоугольнике)
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)    #self аналогичен this, т.е говорим приложению принять разметку vbox
#система сигнал - слот дает соединяет источник события, объект события и цель события, система имитирует сигнал от источника события,
#когда изменяется состояние объекта события, а цель(target) события находится в состоянии ожидания сигнала(является слотом(slot)),
#как только сигнал приходит, таргет меняет свое состояние на соответсвующее поступившему сигналу, а значит и изменившемуся состоянию источника события
#в этом случае источник события - слайдет, объект события - изменение состояния слайдера, таргет - lcd дисплей 
        sld.valueChanged.connect(lcd.display)   #коннект ивент, слайдер меняет -> соединение с lcd -> lcd менят значение

        self.setGeometry(300, 300, 250, 150)    #setGeometry - установления дефолтного размера окна
        self.setWindowTitle('Signal and Slot')  #setWindowTitle - установка заголовка окна
        self.show()

if __name__ == '__main__':      #основная петля для приложения

    app = QApplication(sys.argv)    #приложение - экземпляр класса QApplication
    ex = SigSlot()
    sys.exit(app.exec_())   #выход из основной петли приложения, exec_() применяется для принудительного выхода, без этого не закроется приложение правильно и будут ошибки

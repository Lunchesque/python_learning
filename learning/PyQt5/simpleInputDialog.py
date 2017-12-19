#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *

#QInputDialog предоставляет возможност показать прстое диалоговое окно

class InputDialog(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #создание кнопки для вызова диалогового окна и коннект события
        #нажатия кнопки с методом showDialog, который вызывает диалог
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        #создание текстового поля для принятия значения введенного в
        #диалоговом окне
        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Input Dialog')
        self.show()

        #создание диалогового окна
    def showDialog(self):

        #QInputDialog с помошью своего метода getText принимает себе
        #значение титула окна и сообщения в нем,
        #а также объявялется обработчик (ok, значения типа boolean) для описания действия
        #"OK" в диалоговом окне
        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')

        #если в диалоговм окне нажато "ok" методом setText устанавливается
        #строковое значение текстового поля на главном окне приложения
        if ok:
            self.le.setText(str(text))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = InputDialog()
    sys.exit(app.exec_())

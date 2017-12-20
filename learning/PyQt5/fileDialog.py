#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction,
    QFileDialog, QApplication)
from PyQt5.QtGui import QIcon

class FileDialog(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        openFile = QAction(QIcon('open.png'), '&Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new file')
        openFile.triggered.connect(self.showDialog)

        self.statusBar()

        self.toolbar = self.addToolBar('&Open')
        self.toolbar.addAction(openFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&file')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = FileDialog()
    sys.exit(app.exec_())

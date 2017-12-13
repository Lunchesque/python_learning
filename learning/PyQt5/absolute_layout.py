import sys
from PyQt5.QtWidgets import *

class Absolute(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lbl1 = QLabel('MyLabel', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('ForThis', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('Programm', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Absolute()
    sys.exit(app.exec_())
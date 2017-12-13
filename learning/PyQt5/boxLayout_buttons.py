import sys
from PyQt5.QtWidgets import *

class Buttons(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okBtn = QPushButton('OK')
        cancelBtn = QPushButton('CANCEL')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300 ,350, 200)
        self.setWindowTitle('BoxLayout_buttons')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Buttons()
    sys.exit(app.exec_())

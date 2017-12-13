import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Centering_window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(300, 250)
        self.center()

        self.setWindowTitle('Centered_Window')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Centering_window()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class StatusBar(QMainWindow):
    def __init__(self):
         super().__init__()

         self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Status_Bar')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = StatusBar()
    sys.exit(app.exec_())

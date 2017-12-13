import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class SubMenu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('SubMenu')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = SubMenu()
    sys.exit(app.exec_())

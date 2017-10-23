import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtWidgets import QAction
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *


class Window(QMainWindow):
    """a normal window"""

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("PyQt5")

        extractAction = QAction("Exit", self)
        extractAction.setShortcut("Ctrl+X")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        # show the menubar on MacOS looks like on Windows
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu("File")
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())  # automatically set the button size
        btn.move(100, 100)

        extractAction = QAction("Flee the Screen", self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        self.show()

    def close_application(self):
        choice = QMessageBox.question(self, "Extract!", "Quit???", QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
        	print ("quit application")
        	sys.exit()
        else:
        	pass



def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

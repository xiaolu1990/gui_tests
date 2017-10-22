import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
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
		extractAction.setShortcut("Ctrl+Q")
		extractAction.setStatusTip("Leave the App")
		extractAction.triggered.connect(self.close_application)

		self.statusBar()

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu("File")
		fileMenu.addAction(extractAction)

		self.home()

	def home(self):
		btn = QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.sizeHint())  #automatically set the button size
		btn.move(100, 100)		
		self.show()

	def close_application(self):
		print("Bye Bye")
		sys.exit()

def run():
	app = QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()
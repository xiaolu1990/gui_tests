import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *

class Window(QMainWindow):
	"""a normal window"""
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(100, 100, 400, 400)
		self.setWindowTitle("PyQt5")
		self.home()

	def home(self):
		btn = QPushButton("Quit", self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.sizeHint())  #automatically set the button size
		btn.move(0, 0)		
		self.show()

	def close_application(self):
		print("Bye Bye")
		sys.exit()

def run():
	app = QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()
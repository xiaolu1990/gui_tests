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
		btn.resize(100, 100)
		btn.move(100, 100)
		btn.clicked.connect(QCoreApplication.instance().quit)
		self.show()

app = QApplication(sys.argv)
GUI = Window()

sys.exit(app.exec_())
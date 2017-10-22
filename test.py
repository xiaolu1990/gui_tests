import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
	"""a normal window"""
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(100, 100, 400, 400)
		self.setWindowTitle("PyQt5")
		self.show()

app = QApplication(sys.argv)
GUI = Window()

sys.exit(app.exec_())
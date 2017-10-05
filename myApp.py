# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 17:57:27 2017

@author: xiaolu
"""


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

# subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		# when you subclass a Qt class, you must always call the super __init__ function to allow Qt to set up the object
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("My Awesome App")
		label = QLabel("This is Awesome!")
		# set the widget in the middle of the window
		label.setAlignment(Qt.AlignCenter)
		# setCentralWidget() is a QMainWindow specific function that allows you to set the widget that goesin the middle of the window
		self.setCentralWidget(label)



# You need one (and only one) QApplication instance per application
# Pass in sys.argv to allow command line arguments for your app
# If you know you won't use command line arguments, QApplication([]) workds
app = QApplication(sys.argv)

window = MainWindow()
window.show()

# start the event loop
app.exec_()
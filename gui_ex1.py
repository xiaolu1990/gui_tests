#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:56:35 2017

@author: xiaolu
"""





from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    
    # block for setups of MainWindow
    def __init__(self, *args, **kwargs):
        # When subclass a Qt class you must always call the super __init__ function to allow Qt to set up the objec
        super(MainWindow, self).__init__(*args, **kwargs)
        # change the title of MainWindow
        self.setWindowTitle("My Awesome App")
        # add the widget QLabel
        label = QLabel("This is awesome!!!")
        # place the widget in the middle of MainWindow
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        




# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# allows us to pass command line arguments to our application.
app = QApplication(sys.argv)

#call MainWindow to create the window
window = MainWindow()
#show the window. Window are hidden by default.
window.show()

#start the event loop
app.exec_()


# test for git and github
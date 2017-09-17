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


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# allows us to pass command line arguments to our application.
app = QApplication(sys.argv)

#start the event loop
app.exec_()



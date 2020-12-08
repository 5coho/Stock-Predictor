"""
--main Gui File--

The gui class creates the functionality for the gui.ui file.

Currently underdevelopment

"""


#Metadata
__author__          = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__credits__         = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__email__           = "showes@unbc.ca, velde@unbc.ca"
__python_version__  = "3.9.0"


#imports
import sys
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi


#the seq_gui class
class stock_gui(QWidget):


    #constructor
    def __init__(self):
        super(stock_gui, self).__init__()
        loadUi("GUIs/gui.ui", self)
        self._load_connects()
        self.move(20,20)


    #loads the connection for the buttons
    def _load_connects(self):

        #bttn_create connects
        #self.bttn_openSeq.clicked.connect(self.bttn_openSeq_clicked)
        pass


    #creates the functionality for the Open button
    @pyqtSlot()
    def bttn_openSeq_clicked(self):
        pass

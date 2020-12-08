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
import mplfinance
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from dataFetch import dataFetch
from datetime import date
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.uic import loadUi


#the seq_gui class
class stock_gui(QWidget):


    #constructor
    def __init__(self):
        super(stock_gui, self).__init__()
        loadUi("GUIs/gui.ui", self)
        self._load_connects()
        self.move(20,20)
        self.fetcher = dataFetch()


        #setting the dateEdit_end to current date
        self.dateEdit_end.setDate(QDate(date.today()))

        #populating the stock combobox with symbols
        self._populateComboBox()

        #this is where the data that is grabbed from yfinance goes
        self.data = []


    #loads the connection for the buttons
    def _load_connects(self):

        #bttn_create connects
        self.bttn_plot.clicked.connect(self.bttn_plot_clicked)
        self.bttn_LR_predict.clicked.connect(self.bttn_LR_predict_clicked)


    #creates the functionality for the plot button
    @pyqtSlot()
    def bttn_plot_clicked(self):

        #creating variables from labels
        startDate = self.dateEdit_start.date().toString("yyyy-MM-dd")
        endDate = self.dateEdit_end.date().toString("yyyy-MM-dd")
        symbol = self.comboBox_ticker.currentText()

        #getting the data from dataFetch
        data = self.fetcher.getData(symbol, startDate, endDate)
        #dataList = data.values.tolist()

        mplfinance.plot(data, type='candle', show_nontrading=True, style="yahoo", ylabel="Price", title=f"{symbol} Chart")
        plt.show()


    #creates the functionality for the Linear Regression Predict button
    @pyqtSlot()
    def bttn_LR_predict_clicked(self):
        print("Linear Regression Predict button clicked!", flush=True)


    #this populates the stock symbol combobox with stock symbols
    def _populateComboBox(self):
        symbols = ['AC.TO']
        self.comboBox_ticker.addItems(symbols)
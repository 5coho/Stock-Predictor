"""
--main Gui File--

The gui class creates the functionality for the gui.ui file.

Currently underdevelopment

"""


#Metadata
__author__          = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__credits__         = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__email__           = "showes@unbc.ca, velde@unbc.ca, leary@unbc.ca"
__python_version__  = "3.8.1"


#imports
import sys
import os
from stockPredictor import stockPredictor
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dataFetch import dataFetch
from datetime import date
import numpy as np
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5 import QtWebEngineWidgets


#the seq_gui class
class stock_gui(QWidget):


    #constructor
    def __init__(self):
        super(stock_gui, self).__init__()
        loadUi("GUIs/gui.ui", self)
        self._load_connects()
        self.move(20,20)
        self.fetcher = dataFetch()

        #variables from the stock groupbox
        self.startDate = ""
        self.endDate = ""
        self.symbol = "No Symbol"

        #setting the dateEdit_end to current date
        self.dateEdit_end.setDate(QDate(date.today()))

        #populating the stock combobox with symbols
        self._populateComboBox()

        #setting up plotly environment
        self.browser = QtWebEngineWidgets.QWebEngineView(self)
        self.layout_chart.addWidget(self.browser)

        #this is where the data that is grabbed from yfinance goes
        #is a panda dataFrame Object
        self.data = pd.DataFrame()

        #initializing stock stockPredictor
        self.stockPred = stockPredictor()


    #loads the connection for the buttons
    def _load_connects(self):

        #bttn_create connects
        self.bttn_plot.clicked.connect(self.bttn_plot_clicked)
        self.bttn_LR_predict.clicked.connect(self.bttn_LR_predict_clicked)
        self.bttn_seq2seq_predict.clicked.connect(self.bttn_seq2seq_predict_clicked)


    #creates the functionality for the plot button
    @pyqtSlot()
    def bttn_plot_clicked(self):

        #creating variables from labels
        self.startDate = self.dateEdit_start.date().toString("yyyy-MM-dd")
        self.endDate = self.dateEdit_end.date().toString("yyyy-MM-dd")
        self.symbol = self.comboBox_ticker.currentText()

        #getting the data from dataFetch
        self.data = self.fetcher.getData(self.symbol, self.startDate, self.endDate)
        #dataList = data.values.tolist()

        #plotting data
        self._plotStock(self.data)


    #creates the functionality for the Linear Regression Predict button
    @pyqtSlot()
    def bttn_LR_predict_clicked(self):

        #calling the Linear Regression function
        #storing data to predictionList
        predictionList = self.stockPred.linearRegression(self.data)

        #adding returned values in predictionList to labels
        self.label_LR_openVal.setText(str(round(predictionList[0], 2)))
        self.label_LR_highVal.setText(str(round(predictionList[1], 2)))
        self.label_LR_lowVal.setText(str(round(predictionList[2], 2)))
        self.label_LR_closeVal.setText(str(round(predictionList[3], 2)))



    #creates the functionality for the Linear Regression Predict button
    @pyqtSlot()
    def bttn_seq2seq_predict_clicked(self):

        #calling the seq 2 seq function to get the closing price
        closing = self.stockPred.sequence_to_sequence(self.symbol, self.startDate, self.endDate)

        #printing for testing
        print(closing, flush=True)


    #this populates the stock symbol combobox with stock symbols
    def _populateComboBox(self):
        symbols = ['AC.TO', 'TSLA', 'FTS.TO', 'ENB.TO', 'AMD', 'BTO.TO', 'HSE.TO', 'TRZ.TO', 'NFLX', 'BTO.TO']
        self.comboBox_ticker.addItems(symbols)


    #this function is for plotting the data and adding it to layout_chart
    #is a candlestick chart
    def _plotStock(self, stockData):

        #adding date as a label
        stockData.reset_index(inplace=True,drop=False)

        #plotting figure in layout_chart
        fig = go.Figure(data=[go.Candlestick(x=stockData['Date'],
                open=stockData['Open'],
                high=stockData['High'],
                low=stockData['Low'],
                close=stockData['Close'])])

        #figure layout
        fig.update_layout(title=f"{self.symbol} Chart from {self.startDate} to {self.endDate}",
                yaxis_title='Price',
                xaxis_title='Date')

        #adding to browser widget
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

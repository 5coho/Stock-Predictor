"""
--data fetch file--

This file holds the class that grabs data from the yahoo finance API
basically only has one public function, getData that accesses the Api

"""


#Metadata
__author__          = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__credits__         = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__email__           = "showes@unbc.ca, velde@unbc.ca"
__python_version__  = "3.9.0"


#imports
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd


#the seq_analyzer class
class dataFetch:


    #basically only overrides yfinance to use panads pandas_datareader
    def __init__(self):
        yf.pdr_override()
        pass


    def getData(self, symbol, startDate, endDate):

        #using data reading to get data
        history = pdr.get_data_yahoo(symbol, start=startDate, end=endDate)

        #removes unwanted columns from data
        ohlc = history.iloc[:, [0, 1, 2, 3]]

        return ohlc

"""
--stock predictor file--

This file hold one class, stockPredictor which hold the function relating
to predicting a stock such as Linear Regression

"""

# Metadata
__author__ = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__credits__ = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__email__ = "showes@unbc.ca, velde@unbc.ca, leary@unbc.ca"
__python_version__ = "3.9.0"

# imports
import pandas as pd

import math
import matplotlib.pyplot as plt
import keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping

# the seq_analyzer class
from src.dataFetch import dataFetch


class stockPredictor:

    # do nothing constructor
    def __init__(self):
        pass

    def linearRegression(self, symbol, startDate, endDate):
        pass

    def sequence_to_sequence(self, symbol, startDate, endDate):
        datafetch = dataFetch()
        df = datafetch.getData(symbol, startDate=startDate, endDate=endDate)
        df.reset_index(inplace=True)
        # dataframe creation
        series_data = df.sort_index(ascending=True, axis=0)
        processed_data = pd.DataFrame(index=range(0, len(df)), columns=['Date', 'Close'])
        length_of_data = len(series_data)
        for i in range(0, length_of_data):
            processed_data['Date'][i] = series_data['Date'][i]
            processed_data['Close'][i] = series_data['Close'][i]
        # setting the index again
        processed_data.index = processed_data.Date
        processed_data.drop('Date', axis=1, inplace=True)
        # creating train and test sets using all data in set
        myseriesdataset = processed_data.values
        to_train = myseriesdataset[0:255, :]
        to_valid = myseriesdataset[255:, :]
        # converting dataset into x_train and y_train
        scaler = MinMaxScaler(feature_range=(0, 1))
        scale_data = scaler.fit_transform(myseriesdataset)
        x_train, y_train = [], []
        length_of_totrain = len(to_train)
        for i in range(60, length_of_totrain):
            x_train.append(scale_data[i - 60:i, 0])
            y_train.append(scale_data[i, 0])
        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        # LSTM neural network
        lstm_model = Sequential()
        lstm_model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        lstm_model.add(LSTM(units=50))
        lstm_model.add(Dense(1))
        lstm_model.compile(loss='mean_squared_error', optimizer='adadelta')
        lstm_model.fit(x_train, y_train, epochs=10, batch_size=1, verbose=2)
        # predicting next data stock price
        future_inputs = processed_data[len(processed_data) - (len(to_valid) + 1) - 60:].values
        future_inputs = future_inputs.reshape(-1, 1)
        future_inputs = scaler.transform(future_inputs)
        test_result = []
        for i in range(60, future_inputs.shape[0]):
            test_result.append(future_inputs[i - 60:i, 0])
        test_result = np.array(test_result)
        test_result = np.reshape(test_result,
                                         (test_result.shape[0], test_result.shape[1], 1))
        closing_price_result = lstm_model.predict(test_result)
        closing_price_result = scaler.inverse_transform(closing_price_result)

        return closing_price_result

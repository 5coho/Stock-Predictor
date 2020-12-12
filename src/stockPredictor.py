"""
--stock predictor file--

This file hold one class, stockPredictor which hold the function relating
to predicting a stock such as Linear Regression

"""

# Metadata
__author__ = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__credits__ = "Scott Howes, Braeden Van Der Velde, Tyler Leary"
__email__ = "showes@unbc.ca, velde@unbc.ca, leary@unbc.ca"
__python_version__ = "3.8.1"

# imports

import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None
import datetime as dt
from sklearn.linear_model import LinearRegression
import numpy as np
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from src.dataFetch import dataFetch


class stockPredictor:

    # do nothing constructor
    def __init__(self):
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

    def _dataPrediction(self, data_frame, to_pred):
        x_axis = pd.DataFrame(data_frame.Date)
        y_axis = pd.DataFrame(data_frame[to_pred])
        forecast = x_axis[-1:]
        lm = LinearRegression()
        model = lm.fit(x_axis, y_axis)
        prediction = lm.predict(forecast)
        return prediction[0][0]

    def linearRegression(self, stock_info):
        stock_info.reset_index(inplace=True, drop=False)
        stock_info["Date"] = stock_info["Date"].apply(lambda x: dt.datetime.strftime(x, '%y%m%d'))
        open = self._dataPrediction(stock_info, "Open")
        close = self._dataPrediction(stock_info, "Close")
        high = self._dataPrediction(stock_info, "High")
        low = self._dataPrediction(stock_info, "Low")
        alltogether = [open, high, low, close]
        print(alltogether[0])
        print(alltogether)

# test code
# if __name__ == "__main__":
#     df = dataFetch()
#     pred = stockPredictor()
#     stock_info = df.getData("msft", "2020-01-28", "2020-02-7")
#     pred.linearRegression(stock_info)

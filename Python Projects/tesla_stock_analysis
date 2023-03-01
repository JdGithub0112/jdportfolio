#Import the Python libraries to be used
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM


"""
Data Ingestion and Cleaning
-------------------------------------------------------------------------------
"""


#I'm interested in Tesla data, so I'll create a variable 'company' and assign
#the tesla ticker to it
company = 'TSLA'

#I'll create my date variables, leveraging the datetime libraries
#Create a variable 'start' and assign the first day of this year to it
start = dt.datetime(2023,1,1)
#Create a variable 'end' and set it to whenever 'now' is, also re-format
#this datetime in 12hr format for a more readbile alternative
#(strf = string format)
end = dt.datetime.now()
#.strftime("%I:%M:%S %p")
#print(end)
data = yf.download("TSLA", start = "2023-01-01", end = dt.datetime.now())

tsla = yf.Ticker("TSLA", start = "2023-01-01", end = dt.datetime.now())
tsla.info

#tutorial is based off sentdex youtube channel's finance tutorial playlist
#Tutorial Link: https://pythonprogramming.net/stock-data-manipulation-python-programming-for-finance/

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

#*****UNCOMMENT THE FOLLOWING BLOCK ON CODE TO GET STOCK DATA USING YAHOO API AND DISPLAY A GRAPH OF THAT DATA
style.use('ggplot') #Style of the data
##start = dt.datetime(2000,1,1) #Gets the start time frame for the data, format: YYYY,M,D
##end = dt.datetime(2018,12,31) #Gets the end time frame for the data, format: YYYY,M,D
##df = web.DataReader('TSLA', 'yahoo', start, end) #Gets stock data using pandas_datareader. Format: (stock name, finance api, start, end)
##print (df.head())
##df.plot() #Plots the stock data
##plt.show() #Displays the plot (graph) on screen

#df.to_csv('tsla.csv') #Creates a CSV file containing all stock data, would only need to be ran once per company/stock
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0) #Reads stock data from CSV you've created, different parameters for the data

print (df.head()) #Replace with df.tail() if you want the most recent stock data

#df_zscore = (df - df.mean())/df.std()

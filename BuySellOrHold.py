#Python 3
#!/usr/bin/env python3
import os
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot') #Style of the data

stockName = str(input('Enter Ticker (Stock Symbol): '))
stockTicker = stockName + ".csv" #Takes inputted ticker symbol, makes it capital letters and adds the .csv file extension

def getStockData(stockTicker):
    os.chdir('TickerData/') #Sets the directory path
    if os.path.exists(stockTicker): #If ticker data has been downloaded to our computer, do nothing
        print ("Ticker data for " + stockName + " already exists, reading data from " + stockTicker + ".....")
        pass
    else: # If ticker data doesn't exist on our computer, download the ticker data from the Yahoo API
        try:
            start = dt.datetime(2016,1,1) #Gets the start time frame for the data, format: YYYY,M,D
            #end = dt.datetime(2019,3,1) #Gets the end time frame for the data, format: YYYY,M,D
            end = dt.datetime.today().strftime('%Y-%m-%d')#Gets the end time frame for the data using today's date, format: YYYY,M,D
            df = web.DataReader(stockName, 'yahoo', start, end) #Gets stock data using pandas_datareader. Format: (stock name, finance api, start, end)
            df.to_csv(stockTicker) #Downloads the ticker data to a CSV file
        except:
            print ("Error getting stock data from Yahoo API")
        else:
            print(stockTicker + " was successfully downloaded")

getStockData(stockTicker) #Executes the function

df = pd.read_csv(stockTicker, parse_dates=True, index_col=0) #Reads stock data from CSV you've created, different parameters for the data

df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean() #Calculates the 100 day Moving Average
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=5, colorup='g')
ax1.plot(df.index, df['100ma'], color='blue')

ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
print ("Legend: Blue = 100 Day Moving Average, Green CandleStick = Upward trend (Bull), Red CandleStick = Downward trend (Bear) ")
print ("Trading strategy: Moving Average Crossover. Buy signal: when a stock closes above the Moving Average, buy the next day. Sell Signal: when a stock (open, close, doesn't matter) falls below the Moving Average.")
plt.tight_layout() # Spreads all the axis labels out evenly so no text overlaps
plt.show()



#df_zscore = ((df - df.mean())/df.std())  #Calculates Z value
#print ("Z score is: " + df_zscore)
    

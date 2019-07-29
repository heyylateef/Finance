import os

os.getcwd()
os.chdir('TickerData/')
os.getcwd()
if os.path.exists('AAPL.csv'):
    print ("AAPL.csv ni fi sinu TickerData")
else:
    print ("You jhi messed up son")

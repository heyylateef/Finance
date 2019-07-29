#Python 3
import os
import datetime
from datetime import timedelta

def get_creation_time():
    ago = os.stat('TickerData/GM.csv').st_birthtime
    print(datetime.datetime.fromtimestamp(ago))
    N = 5
    date_N_days_since = datetime.datetime.fromtimestamp(ago) + timedelta(days=N)
    print (date_N_days_since)

    if datetime.datetime.now() >= date_N_days_since:
        print ('Please redownload ticker data')
    else:
        print ('Error')
    
get_creation_time()

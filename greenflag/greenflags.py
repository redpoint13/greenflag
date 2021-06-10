# -*- coding: utf-8 -*-
import helpers
import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web
from datetime import datetime
import pandas_ta as ta

import pyfolio as pf
'''
Pyfolio package provides an easy way to generate a tearsheet containing
performance statistics. These statistics include annual/monthly returns,
return quantiles, rolling beta/Sharpe ratios, portfolio turnover, and a few more.

stock_rets = pf.utils.get_symbol_rets('FB')
pf.create_returns_tear_sheet(stock_rets, live_start_date='2015-12-1')

'''

from zipline.api import order, record, symbol

'''
Zipline is a package that ties the statistics, the data structures,
and the data sources all together.

from zipline.api import order, record, symbol

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price')) 
    
'''



def moving_average(group, n=9):
    sma = pd.rolling_mean(group, n)
    return sma


def moving_average_convergence(group, nslow=26, nfast=12):
    emaslow = pd.ewma(group, span=nslow, min_periods=1)
    emafast = pd.ewma(group, span=nfast, min_periods=1)
    result = pd.DataFrame({'MACD': emafast-emaslow, 'emaSlw': emaslow, 'emaFst': emafast})
    return result

start = datetime(2016, 9, 1)

end = datetime(2018, 9, 1)

# f = web.DataReader('ticker=RGDPUS', 'econdb')
# gs10 = pdr.get_data_fred('GS10')
symbol = 'AAPL.US'  # or 'AAPL.US'

# df = web.DataReader(symbol, 'quandl', '2015-01-01', '2015-01-05')
# f = df.loc['2015-01-02']

sphd = web.DataReader("F", 'yahoo', start, end)
print(sphd)

df_[['emaSlw', 'emaFst', 'MACD']] = sphd.groupby(level=1).Adj_Close.apply(moving_average_convergence)


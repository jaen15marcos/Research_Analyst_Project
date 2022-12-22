#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.stattools import adfuller
import time


num_trades = pd.read_csv(r'/Users/lourdescortes/Downloads/num_trades.csv')   
vol_trades = pd.read_csv(r'/Users/lourdescortes/Downloads/vol_trades.csv')   
val_trades = pd.read_csv(r'/Users/lourdescortes/Downloads/val_trades.csv')   
print(num_trades)

def format_dates(df):
   df['Month'] = pd.to_datetime(df['Month'])
    
def format_num(df, col_name1,col_name2 ):
    df[col_name1] = df[col_name1].astype(str).str.replace(',','')
    df[col_name1] = df[col_name1].astype(str).str.replace('$','')
    df[col_name1] = df[col_name1].astype(float)
    df[col_name2] = df[col_name2].astype(str).str.replace(',','')
    df[col_name2] = df[col_name2].astype(str).str.replace('$','')
    df[col_name2] = df[col_name2].astype(float)


def plot_df(df, x, y, title="", xlabel='', ylabel='', dpi=100):
    plt.figure(figsize=(15,4), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

    
def divide_df(df):
    post = df.iloc[61:94]
    pre = df.iloc[0:61]
    return pre, post

    
num_trades = pd.DataFrame(num_trades, columns=['Month', 'All Traded Marketplaces', 'Toronto Stock Exchange'])
vol_trades = pd.DataFrame(vol_trades, columns=['Month', 'All Traded Marketplaces', 'Toronto Stock Exchange'])
val_trades = pd.DataFrame(val_trades, columns=['Month', 'All Traded Marketplaces', 'Toronto Stock Exchange'])

format_dates(num_trades)
format_dates(vol_trades)
format_dates(val_trades)

format_num(num_trades, 'All Traded Marketplaces', 'Toronto Stock Exchange')
format_num(vol_trades, 'All Traded Marketplaces', 'Toronto Stock Exchange')
format_num(val_trades, 'All Traded Marketplaces', 'Toronto Stock Exchange')

pre_pandemic_num_trades, pandemic_num_trades  = divide_df(num_trades)
pre_pandemic_vol_trades, pandemic_vol_trades = divide_df(vol_trades)
pre_pandemic_val_trades, pandemic_val_trades  = divide_df(val_trades)


plot_df(pre_pandemic_num_trades, x=pre_pandemic_num_trades['Month'], y=pre_pandemic_num_trades['All Traded Marketplaces'], title='Number of Trades From Jan 2015 to Jan 2020')
plot_df(pandemic_num_trades, x=pandemic_num_trades['Month'], y=pandemic_num_trades['All Traded Marketplaces'], title='Number of Trades From Feb 2020 to Nov 2022')

plot_df(pre_pandemic_vol_trades, x=pre_pandemic_vol_trades['Month'], y=pre_pandemic_vol_trades['All Traded Marketplaces'], title='Volume of Trades From Jan 2015 to Jan 2020')
plot_df(pandemic_vol_trades, x=pandemic_vol_trades['Month'], y=pandemic_vol_trades['All Traded Marketplaces'], title='Volume of Trades From Feb 2020 to Nov 2022')

plot_df(pre_pandemic_val_trades, x=pre_pandemic_val_trades['Month'], y=pre_pandemic_val_trades['All Traded Marketplaces'], title='Value of Trades From Jan 2015 to Jan 2020')
plot_df(pandemic_val_trades, x=pandemic_val_trades['Month'], y=pandemic_val_trades['All Traded Marketplaces'], title='Value of Trades From Feb 2020 to Nov 2022')



val_trades.to_csv(r'/Users/lourdescortes/Downloads/1.csv')
num_trades.to_csv(r'/Users/lourdescortes/Downloads/2.csv')
vol_trades.to_csv(r'/Users/lourdescortes/Downloads/3.csv')





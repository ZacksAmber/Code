#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: Quantitative Trading.py                                               #
# File: /Users/zacks/Desktop/Code/Python/Quantitative Trading.py               #
# Project: /Users/zacks/Desktop/Code/Python                                    #
# Created Date: 2020-03-18                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-03-18 8:42:42 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

import datetime
import yfinance as yf
import numpy as np
import pandas as pd

# Create a row and add it to df
def newData(company):
    info = yf.Ticker(company).info
    closePrice(company)

    l = []
    l.append(info['shortName']) # Name
    l.append(info['symbol']) # Symbol
    l.append(getClosePrice) # Price
    l.append(getClosePrice) # Close
    l.append(info['fiftyTwoWeekHigh']) # 52wk High Price
    l.append(info['fiftyTwoWeekLow']) # 52wk Low Price
    l.append(info['marketCap']) # Mkt Cap
    l.append(getClosePrice * info['floatShares']) # Float Cap
    '''
    l.append(info['floatShares']) # Shares
    l.append(info['volume']) # Volume
    l.append(info['averageVolume']) # Avg Volume
    l.append(info['averageVolume10days']) # 10 days Avg Volume
    '''
    if 'trailingPE' in info:
        l.append(round(info['trailingPE'], 2)) # PE
    else:
        l.append(-1)
    if info['priceToBook'] != None:
        l.append(round(info['priceToBook'], 2)) # PB
    else:
        l.append(-1)
    l.append(info['trailingEps']) # EPS
    # l.appen(info[]) # ROE
    l.append(round(info['volume']/info['averageVolume'], 1)) # V/Avg V
    l.append(round(info['volume']/info['averageVolume10days'], 1)) # V/10 Avg V
    l.append(round(getClosePrice/info['fiftyTwoWeekHigh'], 1)) # P/H
    l.append(round(getClosePrice/info['fiftyTwoWeekLow'], 1)) # P/L

    df.loc[len(df)] = l # Add a row to the last row of df

# Get Close Price
def closePrice(symbol):
    global getClosePrice
    getClosePrice = yf.download(symbol, start = datetime.date.today().isoformat())
    getClosePrice = round(getClosePrice['Close'][0], 2)

# Create dataframe "Target Mean", "Target High", "Target Low"
df = pd.DataFrame(columns = ["Name", "Symbol", "Price", "Close", "52wk High Price", "52wk Low Price", "Mkt Cap", "Float Cap", "PE", "PB", "EPS", "V/Avg V", "V/10 Avg V", "P/H", "P/L"])

# Define companies #  "UAL"
companies = ["GOOG", "AMZN", "AAPL", "DIS", "ADM", "BG", "CAT", "BAC", "AXP", "BA", "DAL", "ALK", "JBLU", "TSLA"]

# Main
for i in companies:
    newData(i)

# Export csv
name = "Stock Analysis " + datetime.datetime.now().strftime("%Y-%m-%d") + ".csv"
path = "/Users/zacks/Desktop/Code/Python/Stock Analysis/"
df.to_csv(path + name, index = False)






'''
newData("TSLA")
df

info = yf.Ticker("BG").info
info
df


if 'trailingPE' in info:
    print(1)
else:
    print(0)






stock = yf.Ticker("GOOG, APPL")
stock.info



closePrice(info['symbol'])

617973288 * priceClose['Close'][0]

'shortName'
'symbol'

'floatShares'
'marketCap'


'volume'
'averageVolume'
'averageDailyVolume10Day'
'averageVolume10days'
'regularMarketVolume'
'trailingPE'
'priceToBook

'netIncomeToCommon'
'enterpriseToRevenue': 4.114
'profitMargins': 0.21218








msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
stock.major_holders

# show institutional holders
stock.institutional_holders

# show balance heet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# get option chain for specific expiration
opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts


import yfinance as yf
data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")
data

import yfinance as yf
data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30",
                   group_by="ticker")
data.info
'''
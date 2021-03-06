#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: stocks.py                                                             #
# File: /Users/zacks/Desktop/Code/Python/Crawler/stocks.py                     #
# Project: /Users/zacks/Desktop/Code/Python/Crawler                            #
# Created Date: 2020-06-02                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-06-02 8:48:03 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

import requests
import html5lib
import lxml
import re
import pandas as pd
import os
import datetime
import traceback
from bs4 import BeautifulSoup
from IPython.display import HTML

def yf(stock):
    urls = {}

    urls["yfSummary"] = "https://finance.yahoo.com/quote/{0}?p={0}".format(stock)
    urls["yfStatistics"] = "https://finance.yahoo.com/quote/{0}/key-statistics?p={0}".format(stock)
    urls["yfHistoricalData"] = "https://finance.yahoo.com/quote/{0}/history?p={0}".format(stock)
    # HistoricalData = https://query1.finance.yahoo.com/v7/finance/download/{0}?period1=1559535430&period2=1591157830&interval=1d&events=history
    # hour 17, minute 0
    urls["yfProfile"] = "https://finance.yahoo.com/quote/{0}/profile?p={0}".format(stock)
    urls["yfFinancials"] = "https://finance.yahoo.com/quote/{0}/financials?p={0}".format(stock)
    urls["yfAnalysis"] = "https://finance.yahoo.com/quote/{0}/analysis?p={0}".format(stock)
    urls["yfHolders"] = "https://finance.yahoo.com/quote/{0}/holders?p={0}".format(stock)

    return urls

def getHTMLText(url):
    pass

def getStockList(stock_list, stockURL):
    pass

def getStockInfo(stock_list, stockURL, fpath):
    pass

def main():
    stock_list_url
    stock_info_url
    
    getStockList()
    getStockInfo

stock = "ZM"
url = yf(stock)


# Stock Summary yf(stock)["yfSummary"], which contains 2 tables
stockSummary_t1 = pd.read_html(url["yfSummary"])[0]
stockSummary_t2 = pd.read_html(url["yfSummary"])[1]


# Stock Statistics
pd.read_html(url["yfStatistics"])[0] # Valuation Measures
pd.read_html(url["yfStatistics"])[1] # Stock Price History
pd.read_html(url["yfStatistics"])[2] # Share Statistics
pd.read_html(url["yfStatistics"])[3] # Dividends & Splits
pd.read_html(url["yfStatistics"])[4] # Fiscal Year
pd.read_html(url["yfStatistics"])[5] # Profitability
pd.read_html(url["yfStatistics"])[6] # Management Effectiveness
pd.read_html(url["yfStatistics"])[7] # Income Statement
pd.read_html(url["yfStatistics"])[8] # Balance Sheet
pd.read_html(url["yfStatistics"])[9] # Cash Flow Statement

# Stock Historical Data
pd.read_html(url["yfHistoricalData"])[0] # Valuation Measures

# Stock Financials
# pd.read_html(url["yfFinancials"])[0]

# Stock Analysis
pd.read_html(url["yfAnalysis"])[0] # Earnings Estimate
pd.read_html(url["yfAnalysis"])[1] # Revenue Estimate
pd.read_html(url["yfAnalysis"])[2] # Earnings History
pd.read_html(url["yfAnalysis"])[3] # EPS Trend
pd.read_html(url["yfAnalysis"])[4] # EPS Revisions
pd.read_html(url["yfAnalysis"])[5] # Growth Estimates


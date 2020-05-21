#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: Quantitative Trading IEX.py                                           #
# File: /Users/zacks/Desktop/Code/Python/Stock Analysis/Quantitative Trading IEX.py#
# Project: /Users/zacks/Desktop/Code/Python/Stock Analysis                     #
# Created Date: 2020-03-19                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-03-19 10:40:03 am                                        #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

# Related Package
# pip install iexfinance

# Import Modules
import datetime
import requests, json
import numpy as np
import pandas as pd
from iexfinance.stocks import Stock
from iexfinance.account import allow_pay_as_you_go
from iexfinance.account import disallow_pay_as_you_go

# Import content
def content(companies_list):
    # Define TOKEN
    TOKEN = "pk_9f21ff865a7b4f5885c420b6101a8075"

    # allow_pay_as_you_go(token=TOKEN)
    # disallow_pay_as_you_go(TOKEN)

    # define query info
    companies = Stock(companies_list, token=TOKEN, output_format="pandas")

    # define dataframe copies
    companies_quote = companies.get_quote().copy()
    companies_balance_sheet = companies.get_balance_sheet(period="annual").copy()
    # companies_advanced_stats = companies.get_advanced_stats().copy()
    companies_key_stats = companies.get_key_stats().copy()
    companies_cash_flow = companies.get_cash_flow(period="annual").copy()

    # fill null
    companies_quote.fillna(-1, inplace=True)
    companies_balance_sheet.fillna(-1, inplace=True)
    companies_key_stats.fillna(-1, inplace=True)
    companies_cash_flow.fillna(-1, inplace=True)

    # import content
    df["Name"] = companies_quote.loc["companyName"] # Name
    df["Symbol"] = companies_quote.loc["symbol"] # Symbol
    df["Mkt Cap"] = companies_quote.loc["marketCap"] # Market Captical
    df["Price"] = companies_quote.loc["latestPrice"] # Price
    df["Previous Close"] = companies_quote.loc["previousClose"] # Previous Close
    df["52wk High Price"] = companies_quote.loc["week52High"] # 52wk High Price
    df["52wk Low Price"] = companies_quote.loc["week52Low"] # 52wk Low Price

    # P/B
    # Url setting
    base_url = "https://cloud.iexapis.com/stable/stock/market/batch?symbols="
    types = "&types=advanced-stats&token="
    complete_url = base_url + str(companies_list) + types + TOKEN

    # get method of requests module 
    # return response object 
    response = requests.get(complete_url)

    PBR = []
    for i in companies_list:
        PBR.append(response.json()[i]["advanced-stats"]["priceToBook"])
    df["P/B"] = PBR # P/B

    df["P/E"] = companies_quote.loc["peRatio"] # P/E

    PEH = []
    for i in companies_list:
        PEH.append(response.json()[i]["advanced-stats"]["peHigh"])
    df["PEH"] = PEH # PEH

    PEL = []
    for i in companies_list:
        PEL.append(response.json()[i]["advanced-stats"]["peLow"])
    df["PEL"] = PEL # PEL   

    df["EPS"] = companies_key_stats.loc["ttmEPS"] # EPS
    df["Current Ratio"] = np.array(companies_balance_sheet.loc["currentAssets"]) / np.array(companies_balance_sheet.loc["totalCurrentLiabilities"]) # Current Ratio
    df["Debt Ratio"] =  np.array(companies_balance_sheet.loc["totalLiabilities"]) / np.array(companies_balance_sheet.loc["totalAssets"]) # Debt Ratio
    df["ROE"] = np.array(companies_cash_flow.loc["netIncome"]) / np.array(companies_balance_sheet.loc["shareholderEquity"]) # ROE
    df["ROA"] = np.array(companies_cash_flow.loc["netIncome"]) / np.array(companies_balance_sheet.loc["totalAssets"]) # ROA
    df["Vol/30 Avg Vol"] = companies_quote.loc["volume"] / companies_quote.loc["avgTotalVolume"] # "Vol/30 Avg Vol"
    df["Vol/10 Avg Vol"] = companies_quote.loc["volume"] / companies_key_stats.loc["avg10Volume"] # "Vol/10 Avg Vol"
    #df["P/H"] = companies_quote.loc["latestPrice"] / companies_quote.loc["week52High"] # P/H
    #df["PE/PEH"] = df["P/E"] / df["PEH"] # PE/PEH
    #df["P/L"] = companies_quote.loc["latestPrice"] / companies_quote.loc["week52Low"] # P/L
    #df["PE/PEL"] = df["P/E"] / df["PEL"] # PE/PEL
    #df["H/P"] = companies_quote.loc["week52High"] / companies_quote.loc["latestPrice"] # H/P
    #df["PEH/PE"] = df["PEH"] / df["P/E"] # PEH/PE
    #df["L/P"] = companies_quote.loc["week52Low"] / companies_quote.loc["latestPrice"] # H/L
    #df["PEL/PE"] = df["PEL"] / df["P/E"] # PEL/PE
    df["P Position"] = (companies_quote.loc["latestPrice"] - companies_quote.loc["week52Low"]) / (companies_quote.loc["week52High"] - companies_quote.loc["week52Low"]) # Position 
    df["P/E Position"] = (df["P/E"] - df["PEL"]) / (df["PEH"] - df["PEL"]) # P/E Position

    # Data Clean
    data = df.convert_dtypes() # Convert the DataFrame to use best possible dtypes. 
    data.iloc[:, 3:] = data.iloc[:, 3:].round(2) # round numeric part of the dataframe

    # Export csv
    name = "Stock Analysis " + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".csv"
    path = "/Users/zacks/Desktop/Code/Python/Stock Analysis/"
    data.to_csv(path + name, index=False)

# define query list
companies_list = ["CCL", "RCL", "LMT", "BA", "LUV", "DAL", "AAL", "UAL", "JBLU", "ALK", "ADM", "BG", "CAT", "V", "BAC", "AXP", "JPM", "GS", "AAPL", "AMZN", "GOOG", "FB", "MSFT", "TSLA", "DIS", "GILD", "MMM", "KO", "NKE", "UAA"]

# Create dataframe "Target Mean", "Target High", "Target Low"
df = pd.DataFrame(columns=["Name", "Symbol", "Mkt Cap", "Price", "Previous Close", "52wk High Price", "52wk Low Price", "P/B", "P/E", "PEH", "PEL", "EPS", "Current Ratio", "Debt Ratio", "ROE", "ROA", "Vol/30 Avg Vol", "Vol/10 Avg Vol", "P Position", "P/E Position"]) # "P/H", "PE/PEH", "P/L", "PE/PEL", "H/P", "PEH/PE", "L/P", "PEL/PE", 

content(companies_list)





# 自动化类型转变
# 负债表输出

88/(91+85)

1110/1532

(1110-1013)/(1532-1013)
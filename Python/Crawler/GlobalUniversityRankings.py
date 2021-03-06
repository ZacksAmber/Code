#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: GlobalUniversityRankings.py                                           #
# File: /Users/zacks/Desktop/Code/Python/Crawler/GlobalUniversityRankings.py   #
# Project: /Users/zacks/Desktop/Code/Python/Crawler                            #
# Created Date: 2020-05-20                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-11-06 10:38:44 pm                                        #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################
# This program returns the newest U.S News Global University Rankings

import requests
import re
import bs4
from bs4 import BeautifulSoup

import datetime
import pandas as pd

import os

robots = "https://www.usnews.com/robots.txt"

# 1. Get the webpage
def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return r.status_code

# 2. Extract the information
def fillUniversityList(df, html):
    uinfo = []
    soup = BeautifulSoup(html, "html.parser")
    #results = soup.find("div", id=("rankings")).find_all("div", attrs="sep") # locate the result area
    results = soup.find("div", id=("rankings")).find_all("div", attrs="sep")

    if isinstance(results, bs4.element.ResultSet):
        for i in range(len(results)):
            # Rank
            '''
            rank = results[i].find("span", attrs="rankscore-bronze").string
            rank = re.findall(r"\d+\.?\d*", str(rank.string)) # convert to a list
            rank = int(rank[0]) # extract the first element that is int
            '''
            rank = results[i].find("span", attrs="rankscore-bronze")
            rank = rank.find(text=re.compile("\d"))
            rank = str(rank)
            rank = re.search(r"\d+", rank)
            rank = rank.group(0)
            rank = int(rank)

            # Name
            name = results[i].find("h2", "h-taut").find("a").string
            
            # Global Score
            globalScore = float(results[i].find("div", text="Global Score").previous_sibling.previous_sibling.string)

            # Country
            country = results[i].find("div", attrs=["t-taut"]).find("span").string

            # City, State
            cityState = results[i].find("div", attrs=["t-taut"]).find("span", attrs=re.compile("t-dim")).string

            # Link
            link = results[i].find("h2", "h-taut").find("a").get("href")

            uinfo.append([
                rank,
                name,
                globalScore,
                country,
                cityState,
                link
            ])
    else:
        print("error: results <- soup <- request")

    # add the list to the dataframe last row
    for i in uinfo:
        df.loc[len(df), :] = i

    return df

# 3. Output the result
def printUniversityRank(df):
    return df

# 4. OR Export the result as .csv
def exportUniversityRank(df):
    # Export csv
    name = "U.S News Global University Rankings " + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".csv"
    path = os.getcwd()
    df.to_csv(path + name, index=False)

# Main function
def main():
    baseurl = "https://www.usnews.com/education/best-global-universities/rankings"
    page = "?page="

    df = pd.DataFrame(columns=["Rank", "Name", "Global Score", "Country", "City, State", "Link"])

    for i in range(1, 21):
        url = baseurl + page + str(i)
        html = getHTMLText(url)
        result = fillUniversityList(df, html)
    
    return printUniversityRank(result)
    #exportUniversityRank(result)

main()


'''
# Locations of Tags
url = "https://www.usnews.com/education/best-global-universities/rankings"

# Result Area
results = soup.find_all("div", id=("resultsMain")).find_all("div", attrs="sep")
'''
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: ebay.py                                                               #
# File: /Users/zacks/Desktop/Code/Python/Crawler/ebay.py                       #
# Project: /Users/zacks/Desktop/Code/Python/Crawler                            #
# Created Date: 2020-06-02                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-11-13 10:50:29 pm                                        #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

# This program returns the goods you are interested in from ebay.com

# target
# Gundam Fix Figuration Metal Composite

# page 1
# https://www.ebay.com/sch/i.html?_from=R40&_nkw=Gundam+Fix+Figuration+Metal+Composite&_sacat=0&LH_TitleDesc=0&_pgn=1

# page 2
# https://www.ebay.com/sch/i.html?_from=R40&_nkw=Gundam+Fix+Figuration+Metal+Composite&_sacat=0&LH_TitleDesc=0&_pgn=2

# page 3
# https://www.ebay.com/sch/i.html?_from=R40&_nkw=Gundam+Fix+Figuration+Metal+Composite&_sacat=0&LH_TitleDesc=0&_pgn=3

import requests
import re
import pandas
from bs4 import BeautifulSoup

import datetime
import pandas as pd

import os

from IPython.display import HTML

# robots.txt
# robots = "https://ebay.com/robots.txt"

# 1. Get the webpage
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error in getHTML()"

# 2. Extract the informatio
def parsePage(df, html):
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.find("div", re.compile("srp-river-result"))

    # content of 1 page
    for i in soup.find_all("li", re.compile("s-item")):
        row = []

        try:
            row.append(i.find("h3", "s-item__title").string) # title
        except None:
            row.append(i.find("h3", "s-item__title").find("span", "LIGHT_HIGHLIGHT").string)
        row.append(i.find("span", "SECONDARY_INFO").string) # condition
        row.append(i.find("span", "s-item__price").string) # price
        try:
            row.append(i.find("span", "s-item__purchase-options-with-icon").string) # purchase option
        except AttributeError:
            row.append(i.find("span", "s-item__bids s-item__bidCount").string) # or bid counts
        row.append(i.find("span", "s-item__shipping s-item__logisticsCost").string) # shipping cost

        link = i.find("div", "s-item__image-section").find("div", "s-item__image").a.get("href") # image
        row.append("<a href='{0}'>link</a>".format(link))
        df.loc[len(df), :] = row
    
    #df['url'] = df['url'].apply(lambda x: '<a href="http://example.com/{0}">link</a>'.format(x))
    
    return df

# 3. Output the results
def printResults(results):
    results = HTML(results.to_html(escape=False))
    return results

# 4. OR Export the result as .html
def exportResults(goods, results):
    #results = HTML(results.to_html(escape=False))
    file_name = goods + "-" + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".csv"
    path = os.getcwd() # export to the current working directory
    results.to_csv(path + "/" + file_name, index=True)

# Main function
def main():
    goods = input("Please input your target goods: ")
    depth = input("How many pages do you prefer: ")
    depth = int(depth)
    #depth = int(depth)
    #goods = "Gundam Fix Figuration Metal Composite"

    start_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + goods
    df = pd.DataFrame(columns=["Name", "Condition", "Price", "Purchase Option", "Shipping Cost", "url"])

    for i in range(1, depth+1):
        #url = start_url + "&_sacat=0&LH_TitleDesc=0&_pgn=" + str(i)
        url = start_url + "&_pgn=" + str(i)
        html = getHTMLText(url)
        results = parsePage(df, html)
        print("\rCurrent Process: {: .2f}%".format(i*100/depth), end="")

    #return printResults(results)
    exportResults(goods, results)

main()

'''
goods = "Gundam Fix Figuration Metal Composite"
depth = 3
start_url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + goods

url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=Gundam+Fix+Figuration+Metal+Composite&_sacat=0&LH_TitleDesc=0&_pgn=1"

r = requests.get(url, timeout = 30)
r.raise_for_status()
r.encoding = r.apparent_encoding

soup = BeautifulSoup(r.text, "html.parser")
soup = soup.find("div", re.compile("srp-river-result"))


# content of 1 page
for i in soup.find_all("li", re.compile("s-item")):
    #print(i.find("div", "s-item__image-section").find("div", "s-item__image").a.get("href")) # image
    print(i.find("h3", "s-item__title").string) # title
    print(i.find("div", "s-item__subtitle").find("span", "SECONDARY_INFO").string) # condition
    print(i.find("div", "s-item__details clearfix").find("span", "s-item__price").string) # price
    print(i.find("div", "s-item__details clearfix").find("span", re.compile("s-item__purchase-options-with-icon")).string) # purchase option
    print(i.find("div", "s-item__details clearfix").find("span", "s-item__shipping s-item__logisticsCost").string) # shipping cost
    print("")

url

for i in soup.find_all("li", re.compile("s-item")):
    row = []
    #print(i.find("div", "s-item__image-section").find("div", "s-item__image").a.get("href")) # image
    row.append(i.find("h3", "s-item__title").string) # title
    row.append(i.find("div", "s-item__subtitle").find("span", "SECONDARY_INFO").string) # condition
    row.append(i.find("div", "s-item__details clearfix").find("span", "s-item__price").string) # price
    row.append(i.find("div", "s-item__details clearfix").find("span", re.compile("s-item__purchase-options-with-icon")).string) # purchase option
    row.append(i.find("div", "s-item__details clearfix").find("span", "s-item__shipping s-item__logisticsCost").string) # shipping cost
    df.loc[len(df), :] = row
'''

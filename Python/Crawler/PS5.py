#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: PS5.py                                                            #
# File Path: /PS5.py                                                           #
# Created Date: 2020-11-13                                                     #
# -----                                                                        #
# Company: Pluralpoint Group Inc.                                              #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-11-13 11:00:38 pm                                        #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Pluralpoint Group Inc.                                    #
################################################################################

import requests
import re
import pandas
from bs4 import BeautifulSoup as bf

import datetime
import pandas as pd

import os

from IPython.display import HTML

amazon_url = 'https://www.amazon.com/dp/B08FC5L3RG/?coliid=ILK58YOE0GSUQ&colid=3NNDLJYT41P5P&psc=0&ref_=lv_ov_lig_dp_it'

amazon_sample = 'https://www.amazon.com/New-Apple-Watch-GPS-44mm-Aluminum/dp/B08J5MK16F/ref=sr_1_2?dchild=1&keywords=Apple+Watch+6&qid=1605336938&sr=8-2'

# 1. Get the webpage
def getHTMLText(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
        r = requests.get(amazon_sample, timeout = 30, headers=headers)
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


amazon_sample

###
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
    r = requests.get(amazon_sample, timeout = 30, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    r.text
except:
    print("Error in getHTML()")

# 2. Extract the information
soup = bf(r.text, "html.parser")
soup.find('div', id='addToCart_feature_div')
soup = soup.find("div", re.compile("addToCart_feature_div"))

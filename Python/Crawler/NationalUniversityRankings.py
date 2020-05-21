#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: NationalUniversityRankings.py                                         #
# File: /Users/zacks/Desktop/Code/Python/Crawler/NationalUniversityRankings.py #
# Project: /Users/zacks/Desktop/Code/Python/Crawler                            #
# Created Date: 2020-05-20                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-05-20 7:30:24 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################
# This program returns the newest U.S News National University Rankings

import requests
import re
import bs4
from bs4 import BeautifulSoup

import datetime
import pandas as pd

robots = "https://www.usnews.com/robots.txt"

# 1. Get the webpage
def getHTMLText(url):
    try:
        # global r
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
    results = soup.find("ol", attrs=re.compile("ResultsCards")).find_all("li", id=re.compile("school")) # locate the result area

    if isinstance(results, bs4.element.ResultSet):
        for i in range(len(results)):
            # Rank
            rank = results[i].find("div", "ranked").find("strong").string
            rank = re.findall(r"\d+\.?\d*", str(rank.string)) # convert to a list
            rank = int(rank[0]) # extract the first element that is int

            # Name
            name = results[i].find("h3", "Heading-bocdeh-1").find("a").string

            # Address
            addr = results[i].find("div", attrs=re.compile("DetailCardColleges__CardOverview")).find("div").find("p").string

            # Tuition
            tuition = results[i].find("div", attrs=re.compile("DetailCardColleges__CardStats")).find("dt", text="Tuition and Fees").next_sibling.string

            # Enrollment
            enrollment = results[i].find("div", attrs=re.compile("DetailCardColleges__CardStats")).find("dt", attrs="label-wrapper", text="Enrollment").next_sibling.string

            # Link
            link = results[i].find("h3", "Heading-bocdeh-1").find("a").get("href")

            uinfo.append([
                rank,
                name,
                addr,
                tuition,
                enrollment,
                link
            ])
    else:
        print("error: results <- soup <- request")

    for i, j in zip(uinfo, range(len(uinfo))):
        df.loc[j, :] = i

    return df


# 3. Output the result
def printUniversityRank(df):
    return df

# 4. OR Export the result as .csv
def exportUniversityRank(df):
    # Export csv
    name = "U.S News National University Rankings " + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".csv"
    path = "/Users/zacks/Desktop/Code/Python/Crawler/"
    df.to_csv(path + name, index=False)

# Main function
def main():
    url = "https://www.usnews.com/best-colleges/rankings/national-universities"
    df = pd.DataFrame(columns=["Rank", "Name", "Address", "Tuition", "Enrollment", "Link"])

    html = getHTMLText(url)
    result = fillUniversityList(df, html)
    
    #return printUniversityRank(result)
    exportUniversityRank(result)

main()


'''
# Locations of Tags
url = "https://www.usnews.com/best-colleges/rankings/national-universities"

# Result Area
soup = soup.find("ol", attrs=re.compile("ResultsCards"))
print(soup.find("li").prettify())
'''
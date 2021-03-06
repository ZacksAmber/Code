#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: crawler2.py                                                           #
# File: /Users/zacks/Desktop/Code/Python/Crawler/crawler2.py                   #
# Project: /Users/zacks/Desktop/Code/Python/Crawler                            #
# Created Date: 2020-05-20                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-05-20 1:05:39 am                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

import requests
import re
from bs4 import BeautifulSoup as bf

keyword = "Tesla"

url_google = "http://www.google.com/search"
kv_google = {'q': keyword}

r = requests.get(url_google, params = kv_google)
r.status_code
soup = bf(r.text, "html.parser")

soup("title")
soup.a.get("href")

for link in soup.find_all(href=re.compile("http")):
    print(link.get("href"))

link.get("href")

soup.find_add("a")

type(soup)

570/600

help(re.match)

help(re.search)

help(re.finditer)


import re

m = re.search(r"\d{5}", "360 Huntington Ave, Boston MA 02115")
if m:
    print(m.group(0))
# 02115

m = re.match(r"\d{5}", "360 Huntington Ave, Boston MA 02115")
if m:
    print(m.group(0))
# 

m = re.match(r"\d{5}", "02115 Huntington Ave, Boston MA")
if m:
    print(m.group(0))
# 02115

m = re.match(r"\d{5}", "02115 Huntington Ave, Boston MA 02115")
if m:
    print(m.group())
# 02115

m = re.findall(r"\d{5}", "02115 Huntington Ave, Boston MA 02115")
if m:
    print(m)
# ['02115', '02115']

for m in re.finditer(r"\d{5}", "02115 Huntington Ave, Boston MA 02115"):
    if m:
        print(m.group(0))
# 02115
# 02115


zipcode = re.compile(r'\d{5}')
for m in re.finditer(zipcode, "02115 Huntington Ave, Boston MA 02115"):
    if m:
        print(m.group(0))
# 02115
# 02115

result = zipcode.search("02115 Huntington Ave, Boston MA 02115")
result.group(0)
# 02115

for result in zipcode.finditer("02115 Huntington Ave, Boston MA 02115"):
    if result:
        print(result.group(0))
# 02115
# 02115

result.start()

help(result.string


zipcode = re.compile(r'\d{5}')
result = zipcode.search("02115 Huntington Ave, Boston MA 02115")

result.string
# '02115 Huntington Ave, Boston MA 02115'

result.re
# re.compile(r'\d{5}', re.UNICODE)

result.pos
# 0

result.endpos
# 37

result.group()
# '02115'

result.start()
# 0

result.end()
# 5

result.span()
# (0, 5)


import re

m = re.search("^P.*", "Python")
if m:
    print(m.group(0))
# Python

import re

m = re.search("^P.*?", "Python")
if m:
    print(m.group(0))
# P


d = 0.22

m = re.search(r"-?\d+\.?\d*", "fasfds ---0.")
m = re.search("\d+\.?\d*", "fasfsdf ---0.22")
m.group(0)


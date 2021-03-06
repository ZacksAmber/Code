#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: crawler1.py                                                           #
# File: /Users/zacks/Desktop/Code/Python/Crawler/crawler1.py                   #
# Project: /Users/zacks/Desktop/Code/Python/Crawler                            #
# Created Date: 2020-05-19                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-05-22 3:19:11 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

import requests
from bs4 import BeautifulSoup as bf

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status() # if status is not 200, it pops up an HTTPError
        r.encoding = r.apparent_encoding
        obj = bf(r.text)
        return obj
        #return r.text
    except:
        return "Error"

url = "https://item.jd.com/2967929.html"
#url = "http://zacks.one"
getHTMLText(url)

url = "https://www.amazon.com/BANDAI-Spirits-KAITAI-SHOU-KI-Mobile-Gundam/dp/B07T24NX2N/ref=sr_1_4?dchild=1&keywords=gundam+rx-93&qid=1589951909&sr=8-4"
r = requests.get(url, headers=kv)
r.status_code
bf(r.text)

r.request.headers

# Search Engine
import requests

keyword = "Tesla"

url_baidu = "http://www.baidu.com/s"
kv_baidu = {'wd': keyword}

url_360 = "http://www.so.com/s"
kv_360 = {'q': keyword}

url_google = "http://www.google.com/search"
kv_google = {'q': keyword}


r = requests.get(url_google, params = kv_google)
r.status_code
bf(r.text[0:1000])
r.request.url

'https://www.google.com/search?q=Tesla'

## Picture
import requests
import os

url = "https://raw.githubusercontent.com/ZacksAmber/PicGo/master/img/20200519161434.png"
root = "/Users/zacks/Downloads/Python Crawler/"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open (path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("Picture Saved!")
    else:
        print("File Existed!")
except:
    print("Scrawling Failed!")

# Search for IP Address
import requests

url = "https://whatismyipaddress.com/ip/"
ip = "1.1.1.1"

try:
    r = requests.get(url+ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:-500])
except:
    print("Scrawling Failed")

# BeautifulSoup
import requests
from bs4 import BeautifulSoup as bf

r = requests.get("https://python123.io/ws/demo.html")
r.text
demo = r.text

bf(demo)
soup = bf(demo, "html.parser")
print(soup.prettify()) 
type(soup)
type(soup.prettify())

soup.title
soup.a # return 1st tag a
tag = soup.a
tag.name # return the name of tag a
tag.parent.name # return the name of a's parent
tag.parent.parent.name # return the name of a's parent's parent
tag.attrs # return the attributes of tag a
tag.attrs['class']
type(tag)
type(tag.attrs)

soup.a.string # return the content of a tag

soup.p
soup.p.string
type(soup.p.string)

newsoup = bf("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
print(newsoup.prettify())
newsoup.b
newsoup.b.string
type(newsoup.b)

newsoup.p
newsoup.p.string
type(newsoup.p)

# Iteration
import requests
from bs4 import BeautifulSoup as bf

r = requests.get("https://python123.io/ws/demo.html")
r.text
demo = r.text

bf(demo)
soup = bf(demo, "html.parser")

# 下行遍历
soup.head
soup.head.contents
soup.body.contents
len(soup.body.contents)
soup.body.contents[1]

# 上行遍历
soup.title.parent
soup.html.parent
soup.parent

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# 平行遍历

soup.a.next_sibling
soup.a.next_sibling.next_sibling
soup.a.previous_sibling
soup.a.parents

## Prettify
import requests
from bs4 import BeautifulSoup as bf

r = requests.get("https://python123.io/ws/demo.html")
r.text
demo = r.text 

bf(demo)
soup = bf(demo, "html.parser")

soup.prettify()
print(soup.prettify())
print(soup.a.prettify())

## Information Extraction
import requests
from bs4 import BeautifulSoup as bf

r = requests.get("https://python123.io/ws/demo.html")
r.text
demo = r.text 

soup = bf(demo, "html.parser")


for link in soup.find_all('a'):
    print(link.attrs)
    print(link)
    print(link.get('href')) # get the attribute of a tag

for tag in soup.find_all(True): # True means all of the tags
    print(tag.name)

import re

for tag in soup.find_all(re.compile('^b')): # start with b
    print(tag.name)

soup.find_all('p', 'course')

soup.find_all(id='link1')
for link in soup.find_all(href=re.compile("http")):
    print(link)

soup.find_all(id='link')
soup.find_all(id=re.compile('link'))

soup.find_all('a', recursive=False)
soup.find_all(string = "Basic Python")
soup.find_all(string = re.compile("Python"))

soup.find_all(string = re.compile("Python")) == soup(string = re.compile("Python"))

tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"

print(tplt.format("排名", "学校名称", "总分", chr(12288))) 

"python" == "python"

re.compile("a*")
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: GE Aviation.py                                                        #
# File: /Users/zacks/Desktop/Code/Python/GE Aviation/GE Aviation.py            #
# Project: /Users/zacks/Desktop/Code/Python/GE Aviation                        #
# Created Date: 2020-02-27                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-02-27 1:36:42 am                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

# Modules import
import mysql.connector
import numpy as np
import pandas as pd
import plotly.express as px

# Define class to connect to MySQL server, and fetch data from MySQL database
class MySQL:
    def __init__(self):
        self.host = "localhost"
        self.user = "test"
        self.passwd = "passwd"
        self.database = "GE"
        self.table = "heat_scores"
        # self.host = input("Input your host: ")
        # self.user = input("Input your user name: ")
        # self.passwd = input("Input your password: ")
        # self.database = input("Input your database: ")
        # self.table = input("Input your database: ")

    def Connect(self):
        import mysql.connector

        self.connect = mysql.connector.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            database = self.database
            )
        
        try:
            self.cursor = self.connect.cursor()
        except AttributeError:
            import mysql.connector
            self.cursor = self.connect.cursor()

    def tmp(self):
        self.__init__()
        self.Connect()
        sql = "SHOW TABLES"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return(result)

p1 = MySQL()
p1.tmp()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: Weather.py                                                            #
# File: /Users/zacks/Desktop/Code/Python/Projects/Weather.py                   #
# Project: /Users/zacks/Desktop/Code/Python/Projects                           #
# Created Date: 2020-02-26                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-02-26 8:32:04 am                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

import datetime
import requests, json

class Weather:
    def __init__(self, location):
        self.location = location

    def API(self):
        # Enter your API key here 
        api_key = "af239eac3d426ff8aa48238038f3e701"

        # base_url variable to store url 
        base_url = "http://api.openweathermap.org/data/2.5/forecast"

        # complete_url variable to store 
        # complete url address 
        complete_url = base_url + "?q=" + self.location + "&appid=" + api_key

        # get method of requests module 
        # return response object 
        response = requests.get(complete_url)

        # json method of response object  
        # convert json format data into 
        # python format data 
        self.x = response.json()

    def Date(self, date = 0):
        self.date = datetime.date.today() + datetime.timedelta(days = date)
        print("Date: " + self.date.isoformat())

    def Location(self):
        print("Location: " + self.location)
        
    def Temperature(self, date = 0):
        # - kelvin unit (273.15)
        self.temp = int(self.x['list'][date]['main']['temp'] - 273.15)
        self.temp_min = int(self.x['list'][date]['main']['temp_min'] - 273.15)
        self.temp_max = int(self.x['list'][date]['main']['temp_max'] - 273.15)

        print("Temperature: " + str(self.temp) + "°C")
        print("Min temperature: " + str(self.temp_min) + "°C")
        print("Max temperature: " + str(self.temp_max) + "°C")
    def Weather(self, date = 0):
        self.weather = self.x['list'][date]['weather'][0]['main']
        
        print("Weather: " + self.weather)

    def Humidity(self, date = 0):
        self.humidity = self.x['list'][date]['main']['humidity']

        print("Humidity: " + str(self.humidity) + "%")

    """ Give up because miss information
    def Rain(self, date = 0):
        self.rain = self.x['list'][date]['rain']['3h']

        print("Chance of Rain: " + self.rain)
    """

    def Summary(self): # Invoke all functions above
        self.API()

        for i in range (6):
            self.Date(i)
            self.Location()
            self.Weather(i)
            self.Temperature(i)
            self.Humidity(i)
    #        self.Rain(i)
            print("")

location = Weather(input("Input Your Location: "))
location.Summary()
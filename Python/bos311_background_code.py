#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Title: bos311_background_code.py
# Created Date: February 06, 2020, 9:18:21 pm
# Author: Danlin Shen(shen.da@husky.neu.edu)
# Github: https://github.com/ZacksAmber/Python
# Copyright (c) 2020 Danlin Shen
###

# Import module
import mysql.connector
import datetime

# Connect to MySQL
mysql_test = mysql.connector.connect(
    host="localhost",
    user="test",
    passwd="passwd",
    database="BOS311"
)

# Define cursor
test_cursor = mysql_test.cursor()

# Create a dict to store user's new case.
case_information = {}

# Define a function to judge if the case is duplicated.
def judge_duplicated():
    sql = "SELECT * FROM test WHERE reason = '{0}' AND location_zipcode = '{1}' AND '{2}'".format(
    case_information['reason'],
    case_information['location_zipcode'],
    case_information['location_street_name']
)

    test_cursor.execute(sql)
    result = test_cursor.fetchall()
    return(result)

# Define a function to judge if the case is Open.
def judge_open():
    sql = "SELECT * FROM test WHERE reason = '{0}' AND location_zipcode = '{1}' AND '{2}' AND case_status = '{3}'".format(
        case_information['reason'],
        case_information['location_zipcode'],
        case_information['location_street_name'],
        case_information['case_status']
    )

    test_cursor.execute(sql)
    result = test_cursor.fetchall()

    if case_information['case_status'] == "Open":
        return(result)
    else:
        result = []

# Define a function to judge if the case is created today.
def judge_date():
    sql = "SELECT * FROM test WHERE reason = '{0}' AND location_zipcode = '{1}' AND '{2}' AND case_status = '{3}' AND open_dt LIKE '{4}%'".format(
        case_information['reason'],
        case_information['location_zipcode'],
        case_information['location_street_name'],
        case_information['case_status'],
        case_information['open_dt']
    )

    test_cursor.execute(sql)
    result = test_cursor.fetchall()

    # today = datetime.datetime.now().date().isoformat()
    today = '2020-01-31' # Assume today is '2020-01-31'

    if case_information['open_dt'] == today:
        return(result)
    else:
        result = []

# Main function.
def main_function():
    if judge_duplicated():
        if judge_open(): # Status 4: Open case
            print("Status 4: This is a duplicated case. You should raise priority!")
        else: # Closed case
            if judge_date():
                print("Status 3: This may not be a new case. You should use AWS Rekognition!")
            else: # Status 2: closed several days ago
                print("Status 2: This is a new case. You should UPDATE database!")
    else: # Status 1: NOT duplicated case
        print("Status 1: This is a new case. You should UPDATE database!")

########
# Test #
########
def status_1(): # NOT duplicated case > Update Database
    case_information['reason'] = "Street Lights"
    case_information['location_zipcode'] = "00000"
    case_information['location_street_name'] = "15 Sudbury St"
    case_information['case_status'] = None
    case_information['open_dt'] = None
    return(case_information)

status_1()
main_function()

def status_2(): # Duplicated case but closed several days ago > New case and Update Database
    case_information['reason'] = "Enforcement & Abandoned Vehicles"
    case_information['location_zipcode'] = "02203"
    case_information['location_street_name'] = "15 Sudbury St"
    case_information['case_status'] = "Closed"
    case_information['open_dt'] = "2020-01-13" # Several days ago
    return(case_information)

status_2()
main_function()

def status_3(): # Duplicated case but closed today > Analyze(Rekognition)
    case_information['reason'] = "Enforcement & Abandoned Vehicles"
    case_information['location_zipcode'] = "02203"
    case_information['location_street_name'] = "15 Sudbury St"
    case_information['case_status'] = "Closed"
    case_information['open_dt'] = "2020-01-31" # Assume today is 2020-01-31
    return(case_information)

status_3()
main_function()

def status_4(): # Duplicated and open case > Raise priority
    case_information['reason'] = "Street Lights"
    case_information['location_zipcode'] = "02203"
    case_information['location_street_name'] = "15 Sudbury St"
    case_information['case_status'] = "Open"
    case_information['open_dt'] = "2020-01-22" # Several days ago
    return(case_information)

status_4()
main_function()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Title: bos311_background_code.py
# Created Date: February 06, 2020, 9:18:21 pm
# Author: Zacks Shen(zacks.shen@gmail.com)
# Github: https://github.com/ZacksAmber
# Blog: https://zacks.one
# Copyright (c) 2020 Zacks Shen
###

# Import modules
import mysql.connector
import datetime

##########################
# Define Query Functions #
##########################
# Define a function to connect MySQL
def mysql_login(mysql_host, mysql_user, mysql_passwd, mysql_database):
    global mysql_connect

    mysql_connect = mysql.connector.connect(
        host = mysql_host,
        user = mysql_user,
        passwd = mysql_passwd,
        database = mysql_database
    )

# Define a function to collect case information
def case(open_dt, case_status, case_title, reason, location, source, email, priority):
    global case_information

    case_information = {
    'case_enquiry_id': None,
    'open_dt': open_dt,
    'target_dt': None,
    'closed_dt': None,
    'ontime': None,
    'case_status': case_status,
    'closure_reason': None,
    'case_title': case_title,
    'subject': None,
    'reason': reason,
    'type': None,
    'queue': None,
    'department': None,
    'submittedphoto': None,
    'closedphoto': None,
    'location': location,
    'fire_district': None,
    'pwd_district': None,
    'city_council_district': None,
    'police_district': None,
    'neighborhood': None,
    'neighborhood_services_district': None,
    'ward': None,
    'precinct': None,
    'location_street_name': None,
    'location_zipcode': None,
    'latitude': None,
    'longitude': None,
    'source': source,
    'email': email,
    'priority:': priority
    }

    return(case_information)

# Define a function to judge if the case is duplicate.
def judge_duplicate():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
    mysql_table,
    case_information['reason'],
    case_information['location']
)

    mysql.execute(sql)
    result = mysql.fetchall()

    if len(result) > 0:
        case_information['priority'] = len(result)
        return(result)
    else:
        case_information['priority'] = 1
        return(result)

# Define a function to judge if the case is Open.
def judge_open():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}' AND case_status = '{3}'".format(
        mysql_table,
        case_information['reason'],
        case_information['location'],
        case_information['case_status']
    )

    mysql.execute(sql)
    result = mysql.fetchall()

    if result[0][5] == "Open": # extract case_status
        return(result)
    else:
        result = []

# Define a function to judge if the case is created today.
def judge_date():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}' AND case_status = '{3}' AND open_dt LIKE '{4}%'".format(
        mysql_table,
        case_information['reason'],
        case_information['location'],
        case_information['case_status'],
        case_information['open_dt']
    )

    mysql.execute(sql)
    result = mysql.fetchall()

    if result[0][1][0:10] == today: # extract the date part from open_dt. e.g, '2020-01-31 14:35:46' > '2020-01-31'
        return(result)
    else:
        result = []

##########################
# Define MySQL Functions #
##########################

# Define the UPDATE function raise the priority
def mysql_update():
    if case_information['priority'] > 5:
        case_information['priority'] = 5
    else:
        case_information['priority']+= 1

    sql = "UPDATE {0} SET priority = {1} WHERE case_status = '{2}' AND reason = '{3}' AND location = '{4}'".format(
        mysql_table,
        case_information['priority'],
        case_information['case_status'],
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    mysql_connect.commit()
    print(mysql.rowcount, "record(s) affected")

# Define the INSERT function to insert new case
def mysql_insert():
    case(
    open_dt = datetime.datetime.now().date().isoformat(),
    case_status = "",
    case_title = "",
    reason = "",
    location = "360 Huntington Ave",
    source = "ChatBot",
    email = "test@gmail.com",
    priority = 100
    )

    sql = "INSERT INTO " + mysql_table + " (case_enquiry_id, open_dt, target_dt, closed_dt, ontime, case_status, closure_reason, case_title, subject, reason, type, queue, department, submittedphoto, closedphoto, location, fire_district, pwd_district, city_council_district, police_district, neighborhood, neighborhood_services_district, ward, precinct, location_street_name, location_zipcode, latitude, longitude, source, email, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (0, datetime.datetime.now().date().isoformat(), None, None, None, 'Open', None, case_information['case_title'], None, case_information['reason'], None, None, None, None, None, case_information['location'], None, None, None, None, None, None, None, None, None, None, None, None, case_information['source'], case_information['email'], 1)

    mysql.execute(sql, val)
    mysql_connect.commit()
    print(mysql.rowcount, "record inserted.")

#################
# Main function #
#################
def main_function():
    if judge_duplicate():
        if judge_open(): # Situation 4: Open case
            print("Situation 4: This is a duplicate case. You should UPDATE database!")
            mysql_update()
        else: # Closed case
            if judge_date():
                print("Situation 3: This may not be a new case. You should use AWS Rekognition!")
            else: # Situation 2: closed several days ago
                print("Situation 2: This is a new case. You should INSERT database!")
                mysql_insert()
    else: # Situation 1: NOT duplicate case
        print("Situation 1: This is a new case. You should INSERT database!")
        mysql_insert()

###################
# Set Information #
###################
# Set login information
mysql_login(
    mysql_host = "localhost",
    mysql_user = "test",
    mysql_passwd = "passwd",
    mysql_database = "BOS311"
    )

# Set MySQL cursor
mysql = mysql_connect.cursor()

# Set MySQL table
mysql_table = 'test_2020'

# Set case information
case(
    open_dt = datetime.datetime.now().date().isoformat(),
    case_status = "",
    case_title = "",
    reason = "",
    location = "360 Huntington Ave",
    source = "ChatBot",
    email = "test@gmail.com",
    priority = 100
)

# Set date (for judge_date())
# today = datetime.datetime.now().date().isoformat()
today = '2020-01-31' # Assume today is '2020-01-31'

########################
# Receive Request JSON #
########################


########
# Test #
########
# Situation 1: NOT duplicate case > INSERT Database
def status_1():
    case(
        open_dt = None,
        case_status = None,
        case_title = "",
        reason = "Test",
        location = "15 Sudbury St  Boston  MA  02203",
        source = "ChatBot",
        email = "test@gmail.com",
        priority = 1
    )

status_1()
main_function()
# SELECT * FROM test_2020 WHERE case_enquiry_id = 0 \G;
# DELETE FROM test_2020 WHERE case_enquiry_id = 0;

# Situation 2: duplicate case but closed several days ago > New case and INSERT database
def status_2():
    case(
        open_dt = "2020-01-13",
        case_status = "Closed",
        case_title = "",
        reason = "Enforcement & Abandoned Vehicles",
        location = "15 Sudbury St  Boston  MA  02203",
        source = "ChatBot",
        email = "test@gmail.com",
        priority = 1
    )

status_2()
main_function()
# SELECT * FROM test_2020 WHERE case_enquiry_id = 0 \G;
# DELETE FROM test_2020 WHERE case_enquiry_id = 0;

# Situation 3: # duplicate case but closed today > Analyze(Rekognition)
def status_3():
    case(
        open_dt = "2020-01-31", # Assume today is 2020-01-31,
        case_status = "Closed",
        case_title = "",
        reason = "Enforcement & Abandoned Vehicles",
        location = "15 Sudbury St  Boston  MA  02203",
        source = "ChatBot",
        email = "test@gmail.com",
        priority = 1
    )

status_3()
main_function()

# Situation 4: duplicate and open case > UPDATE database
def status_4():
    case(
        open_dt = None,
        case_status = "Open",
        case_title = "",
        reason = "Street Lights",
        location = "15 Sudbury St  Boston  MA  02203",
        source = "ChatBot",
        email = "test@gmail.com",
        priority = 1
    )

status_4()
main_function()
# SELECT * FROM test_2020 WHERE priority = 2 \G;
# UPDATE test_2020 SET priority = 1 WHERE priority = 2;
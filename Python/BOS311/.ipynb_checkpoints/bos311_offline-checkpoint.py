#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: bos311_offline.py                                                     #
# File: /Users/zacks/Desktop/Code/Python/BOS311/bos311_offline.py              #
# Project: /Users/zacks/Desktop/Code/Python/BOS311                             #
# Created Date: 2020-02-07                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-02-07 8:48:47 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

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
def case(open_dt, reason, location, case_status = 'Open', case_title = None,  source = 'ChatBot', email = None, priority = 1):
    global case_information

    try:
        case_information
    except NameError:
        pass
    else:
        case_information.clear()

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

# Define a MySQL SELECT function. This function will not be used in this program.
def mysql_select():
    sql = input("Input your SELECT sentence: ")

    mysql.execute(sql)
    result = mysql.fetchall()

    if mysql.rowcount == 0:
        print("Empty set")
    elif mysql.rowcount == 1:
        print("1 row in set")
    else:
        print("{0} rows in set".format(mysql.rowcount))

    return(result)

# Define a function to judge if the case is duplicate.
def judge_duplicate():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
    mysql_table,
    case_information['reason'],
    case_information['location']
    )

    mysql.execute(sql)
    result = mysql.fetchall()

    return(result)

# Define a function to judge if the case is Open.
def judge_open():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
        mysql_table,
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    result = mysql.fetchall()

    l = []
    for i in result:
        if i[5] == 'Open':
            l.append(i)

    if len(l) > 0:
        case_information['priority'] = len(l)

    return(result)

# Define a function to judge if the case is created today.
def judge_date():
    open_dt = case_information['open_dt'][0:10] # Extract the data

    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}' AND open_dt LIKE '%{3}%'".format(
        mysql_table,
        case_information['reason'],
        case_information['location'],
        open_dt
    )

    mysql.execute(sql)
    result = mysql.fetchall()

    l = []
    for i in result:
        l.append(i[1].strftime("%Y-%m-%d %H:%M:%S")[0:10]) # change datetime.datetime type to string first then extract date

    if datetime.datetime.now().date().isoformat() in l:
        return(result)
    else:
        return(None) 

##########################
# Define MySQL Functions #
##########################

# Define the UPDATE function to raise the priority
def mysql_UPDATE_priority():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
        mysql_table,
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    result = mysql.fetchall()

    # Get the priority of the existed case.
    l = []
    for i in result:
        l.append(i[-1])

    if case_information['priority'] + max(l) > 5:
        case_information['priority'] = 5
    else:
        case_information['priority'] = case_information['priority'] + max(l)

    sql = "UPDATE {0} SET priority = {1} WHERE case_status = 'Open' AND reason = '{2}' AND location = '{3}'".format(
        mysql_table,
        case_information['priority'],
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    mysql_connect.commit()
    print(mysql.rowcount, "record(s) affected")

# Define the UPDATE function to change the case_status
def mysql_UPDATE_case_status(case_status):
    case_information['case_status'] = case_status

    sql = "UPDATE {0} SET case_status = '{1}' WHERE reason = '{2}' AND location = '{3}'".format(
        mysql_table,
        case_information['case_status'],
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    mysql_connect.commit()
    print(mysql.rowcount, "record(s) affected")

# Define the INSERT function to insert new case
def mysql_INSERT():
    sql = "INSERT INTO " + mysql_table + " (case_enquiry_id, open_dt, target_dt, closed_dt, ontime, case_status, closure_reason, case_title, subject, reason, type, queue, department, submittedphoto, closedphoto, location, fire_district, pwd_district, city_council_district, police_district, neighborhood, neighborhood_services_district, ward, precinct, location_street_name, location_zipcode, latitude, longitude, source, email, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (0, case_information['open_dt'], None, None, None, 'Open', None, case_information['case_title'], None, case_information['reason'], None, None, None, None, None, case_information['location'], None, None, None, None, None, None, None, None, None, None, None, None, case_information['source'], case_information['email'], 1)

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
            mysql_UPDATE_priority()
        else: # Must be Closed case
            if judge_date(): # Situation 3: closed today days
                print("Situation 3: This may not be a new case. You should use AWS Rekognition!")
            else: # Situation 2: closed several days ago
                print("Situation 2: This is a new case. You should INSERT database!")
                mysql_INSERT()
    else: # Situation 1: NOT duplicate case
        print("Situation 1: This is a new case. You should INSERT database!")
        mysql_INSERT()

###################
# Set Information #
###################
# Set login information
mysql_login(
    mysql_host = "localhost",
    mysql_user = "test",
    mysql_passwd = "passwd",
    mysql_database = "bosbot"
    )

# Set MySQL cursor
mysql = mysql_connect.cursor()

# Set MySQL table
# mysql_table = 'sample_311'
mysql_table = 'sample_311'

########
# Test #
########
# Situation 1: NOT duplicate case > INSERT Database
def situation_1():
    case(
        open_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        case_status = "Open",
        case_title = "Situation 1",
        reason = "Illegal Parking",
        location = "360 Huntington Ave  Boston  MA  02115",
        source = "ChatBot",
        email = "test@gmail.com",
        priority = 1
    )
    return(case_information)

situation_1()
main_function()

# SELECT * FROM sample_311 WHERE case_title  = "Situation 1" \G

mysql_UPDATE_case_status(case_status = "Closed") # Change the case_status of situation 1 from "Open" to "Closed"

# SELECT * FROM sample_311 WHERE case_title = "Situation 1" \G

# Situation 2: duplicate case but closed several days ago > New case and INSERT database
def situation_2():
    case(
        open_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        case_status = "Open",
        case_title = "Situation 2",
        reason = "Enforcement & Abandoned Vehicles",
        location = "15 Sudbury St  Boston  MA  02203",
        source = "ChatBot",
        email = "test@gmail.com",
        priority = 1
    )
    return(case_information)

situation_2()
main_function()
# SELECT * FROM sample_311 WHERE reason = "Enforcement & Abandoned Vehicles" AND location = "15 Sudbury St  Boston  MA  02203" \G
# DELETE FROM sample_311 WHERE case_title  = "Situation 2";

# Situation 3: # duplicate case but closed today > Analyze(Rekognition)
def situation_3():
    case(
        open_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        case_status = "Open",
        case_title = "Situation 3",
        reason = "Illegal Parking",
        location = "360 Huntington Ave  Boston  MA  02115",
        source = "ChatBot",
        email = "test@gmail.com",
        priority = 1
    )
    return(case_information)

situation_3()
main_function()

# SELECT * FROM sample_311 WHERE reason = "Illegal Parking" AND location = "360 Huntington Ave  Boston  MA  02115" \G
# DELETE FROM sample_311 WHERE case_title  = "Situation 1";

# Situation 4: duplicate and open case > UPDATE priority
def situation_4():
    case(
        open_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        case_status = "Open",
        case_title = "Situation 4",
        reason = "Street Lights",
        location = "15 Sudbury St  Boston  MA  02203",
        source = "ChatBot",
        email = "test@gmail.com",
        priority = 1
    )
    return(case_information)

situation_4()
main_function()
# SELECT * FROM sample_311 WHERE priority != 1 \G
# UPDATE sample_311 SET priority = 1 WHERE priority != 1;
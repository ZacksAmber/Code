#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Title: ge.py
# Created Date: February 09, 2020, 10:10:43 pm
# Author: Zacks Shen(zacks.shen@gmail.com)
# Github: https://github.com/ZacksAmber/
# Blog: https://zacks.one
# Copyright (c) 2020 Zacks Shen
###

import mysql.connector
import pandas

# Before you import the GE Aviation in your database.
# Make sure you have a MySQL and Python Environment.
# Also, you need have a basic knowledge of MySQL, Python and Shell.

# Required:
# 1. Download the files you in needed. Then

# Set MySQL Querry
def mysql_login(mysql_host, mysql_user, mysql_passwd, mysql_database):
    global mysql_connect

    mysql_connect = mysql.connector.connect(
        host = mysql_host,
        user = mysql_user,
        passwd = mysql_passwd,
        database = mysql_database
    )


ge_data_dict_alerts = pandas.read_csv("/Users/Zacks/Desktop/Code/Python/GE Aviation/GE obfuscated_demo_data/Data Dictionary Alerts.csv")

ge_data_dict_demographics = pandas.read_csv("/Users/Zacks/Desktop/Code/Python/GE Aviation/GE obfuscated_demo_data/Data Dictionary Demographics.csv")

ge_heat_scores = pandas.read_csv("/Users/Zacks/Desktop/Code/Python/GE Aviation/GE obfuscated_demo_data/heat_scores.csv")

ge_indicator_data = pandas.read_csv("/Users/Zacks/Desktop/Code/Python/GE Aviation/GE obfuscated_demo_data/indicator_pairs_data.csv")

ge_obfuscated_demo_data = pandas.read_csv("/Users/Zacks/Desktop/Code/Python/GE Aviation/GE obfuscated_demo_data/obfuscated_demo_data.csv")

ge_indicator_data.dtypes
"""
CREATE TABLE indicator_data (
alert_escalation_date TEXT,
alert_id_fk BIGINT,
insert_date TEXT,
score BIGINT,
owner_name TEXT,
employee_id BIGINT,
risk_factor DOUBLE,
avg_score BIGINT,
classification TEXT,
hru TEXT,
alert_category TEXT,
alert_type TEXT,
indicator_pairs TEXT
)
"""

LOAD DATA INFILE "/tmp/indicator_pairs_data.csv"
INTO TABLE indicator_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


ge_heat_scores.dtypes

CREATE TABLE heat_scores(
SHARED_INDICATION_NAME TEXT,
SHARED_INDICATOR_APPLICATION TEXT,
SHARED_INDICATOR_ACTIVITY TEXT,
SHARED_INDICATOR_TYPE TEXT,
SHARED_INDICATOR_SUFFIX TEXT,
HEAT_VALUE TEXT
);

LOAD DATA INFILE "/tmp/heat_scores.csv"
INTO TABLE heat_scores
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


ge_obfuscated_demo_data.dtypes
"""
CREATE TABLE obfuscated_demo_data(
employee_id BIGINT,
person_type TEXT,
person_status TEXT,
ge_hire_date TEXT,
city TEXT,
state_name TEXT,
country_name TEXT,
function_group TEXT,
job_function TEXT,
career_band TEXT,
industry_focus_name TEXT
);
"""

LOAD DATA INFILE "/tmp/obfuscated_demo_data.csv"
INTO TABLE obfuscated_demo_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

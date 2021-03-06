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

# Before you import the GE Aviation in your database.
# Make sure you have a MySQL and Python Environment.
# Also, you need have a basic knowledge of MySQL, Python and Shell.

# Requirements:
# 1. Download the files you in needed. Then run the following code in your shell:
#    cp *.csv /tmp
# 2. Your Python needs two modules: mysql-connector-python, pd
#    https://zacks.one/2020/02/05/Python-MySQL/#2.4
# 3. If your MySQL version > 5.6. Make sure you configure it in a right way.
#    https://zacks.one/2020/02/05/Python-MySQL/#2.7
# 4. Create a MySQL database.

import mysql.connector
import pandas as pd
import numpy as np
import plotly.express as px

# Set MySQL login information
mysql_connect = mysql.connector.connect(
    host = "localhost",
    user = "test",
    passwd = "passwd",
    database = "GE"
)

mysql = mysql_connect.cursor()

# Read data from .csv files
ge_heat_scores = pd.read_csv("/tmp/heat_scores.csv")

ge_indicator_data = pd.read_csv("/tmp/indicator_pairs_data updated.csv")
ge_indicator_data['indicator_pairs'] = ge_indicator_data['indicator_pairs'].str.strip()
ge_indicator_data.to_csv("/tmp/indicator_data.csv", index=False)

ge_obfuscated_demo_data = pd.read_csv("/tmp/obfuscated_demo_data.csv")

# Set table columns & Import data from .csv file 
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
);
"""

"""
LOAD DATA INFILE "/tmp/indicator_pairs_data updated.csv"
INTO TABLE indicator_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
"""

ge_heat_scores.dtypes
"""
CREATE TABLE heat_scores(
SHARED_INDICATION_NAME TEXT,
SHARED_INDICATOR_APPLICATION TEXT,
SHARED_INDICATOR_ACTIVITY TEXT,
SHARED_INDICATOR_TYPE TEXT,
SHARED_INDICATOR_SUFFIX TEXT,
HEAT_VALUE TEXT
);
"""

"""
LOAD DATA INFILE "/tmp/heat_scores.csv"
INTO TABLE heat_scores
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
"""

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

"""
LOAD DATA INFILE "/tmp/obfuscated_demo_data.csv"
INTO TABLE obfuscated_demo_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
"""
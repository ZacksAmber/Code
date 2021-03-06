#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: KinesisClickStreamGenerator.py                                    #
# File Path: /KinesisClickStreamGenerator.py                                   #
# Created Date: 2021-01-30                                                     #
# -----                                                                        #
# Company: Zacks Shen                                                          #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2021-01-30 6:27:59 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2021 Zacks Shen                                                #
################################################################################
 
import sys
import json
import boto3
import random
import datetime
import pandas as pd

# Generate random data by package random
def getReferrer():
    x = random.randint(1,5) # randomly generate x from 1 to 5
    x = x*50
    y = x+30 
    data = {}
    data['user_id'] = random.randint(x, y) # # randomly select a number between x and y as 'user_id'
    data['device_id'] = random.choice(['mobile','computer', 'tablet', 'mobile', 'voice', 'AI-ML'])
    data['client_event'] = random.choice(['auto_nav', 'product_checkout', 'electronics_product_detail', 'electronics_products', 'electronics_selection', 'electronics_cart'])
    now = datetime.datetime.now()
    str_now = now.isoformat()
    data['client_timestamp'] = str_now
    return data

# Send data to Kinesis Data Streams
kinesis = boto3.client('kinesis', region_name='us-east-1')
number_of_records = 200
record_count = 0
while record_count < number_of_records:
    data = json.dumps(getReferrer())
    print(data)
    kinesis.put_record(
        StreamName='ClickStream-Kinesis-Data-Streams',
        Data=data,
        PartitionKey='partitionkey'
    )
    record_count += 1

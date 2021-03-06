#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: DynamoDBLoader.py                                                 #
# File Path: /DynamoDBLoader.py                                                #
# Created Date: 2021-01-20                                                     #
# -----                                                                        #
# Company: Zacks Shen                                                          #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2021-01-20 12:27:52 am                                        #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2021 Zacks Shen                                                #
################################################################################

import boto3

# Get the DynamoDB service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

# Instantiate a table resource object without actually
# creating a DynamoDB table in our code. Know that the attributes of
# the table are lazy-loaded: the attribute 
# values are not populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('dynamodb_lab')

# Print out some data about the table.
# This will cause a request to DynamoDB and the table attribute
# values will be set via the response.
print("\ntable creatin date-time {} \n\ntable key schema {}".format(
        table.creation_date_time, table.key_schema))

# Put an item into our table
table.put_item(
   Item={
        'username': 'Amber',
        'first_name': 'Amber',
        'last_name': 'Lyu',
        'age': 20,
        'customer_id': '00000002',
        'order_timestamp': '10-15-2020'
    }
)
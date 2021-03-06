#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: KinesisClient.py                                                  #
# File Path: /KinesisClient.py                                                 #
# Created Date: 2021-01-16                                                     #
# -----                                                                        #
# Company: Zacks Shen                                                          #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2021-01-18 6:03:50 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2021 Zacks Shen                                                #
################################################################################

import boto3
import json
import time




# define your stream name
kpl_stream = 'kinesis-kpl-demo'

# create the Kinesis service reference for your region
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

# get the description of your Kinesis Data Stream
response = kinesis_client.describe_stream(StreamName=kpl_stream)

# use the Kinesis Data Stream description to get the shard ID
shard_id = response['StreamDescription']['Shards'][0]['ShardId']

# create your shard iterator
shard_iterator = kinesis_client.get_shard_iterator(StreamName=kpl_stream, ShardId=shard_id, ShardIteratorType='LATEST')

shard_iterator = shard_iterator['ShardIterator']

# retrieve your first Kinesis Data Streams record
record_response = kinesis_client.get_records(ShardIterator=shard_iterator, Limit=2)

# loop until you have received all of the Kinesis Data Streams records
while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'], Limit=2)

    # add your deaggregation logic here
    # where you will deaggregate the user records from each Kinesis Data Streams record
    # you will then perform actions on your user records, such as storing them on S3, or copying them to a Redshift table
    print(record_response, "\n")

    # wait for 1 second before retrieving the next Kinesis Data Streams record
    time.sleep(1)
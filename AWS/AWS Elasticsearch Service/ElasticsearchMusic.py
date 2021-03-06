#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: ElasticsearchMusic.py                                             #
# File Path: /ElasticsearchMusic.py                                            #
# Created Date: 2021-01-31                                                     #
# -----                                                                        #
# Company: Zacks Shen                                                          #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2021-01-31 3:30:10 am                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2021 Zacks Shen                                                #
################################################################################

import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
import json
from requests_aws4auth import AWS4Auth

host = 'search-music-em7ra7talkkrfuwrits5il2alq.us-east-1.es.amazonaws.com/' # change to your Elasticsearch host name
region = 'us-east-1' # the region where you created your S3 bucket and Elasticsearch cluster
service = 'es'

bulk_file = open('music_bulk.json', 'r').read()

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

response = es.bulk(bulk_file)
print(json.dumps(response, indent=2, sort_keys=True))

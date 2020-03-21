#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# Title: Supervised ML.py                                                      #
# File: /Users/zacks/Desktop/Code/Python/Projects/Supervised ML.py             #
# Project: /Users/zacks/Desktop/Code/Python/Projects                           #
# Created Date: 2020-03-20                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@gmail.com>                                                #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-03-20 4:03:05 pm                                         #
# Modified By: Zacks Shen <zacks.shen@gmail.com>                               #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################


from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot') 
iris = datasets.load_iris()
type(iris)

iris
iris.keys()

iris.data # data
iris.target # classification
iris.target_names # classification names

X = iris.data
y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names)

_ = pd.plotting.scatter_matrix(df, c = y, figsize = [8, 8], s=150, marker = 'D')



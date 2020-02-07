#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Title: ALY6050.py
# Created Date: December 29, 2019, 11:04:12 pm
# Author: Danlin Shen(shen.da@husky.neu.edu)
# Github: https://github.com/ZacksAmber/R
# Copyright (c) 2019 Danlin Shen
###

## CHAPTER 2
### 2.5 Descriptive Statistics for Numerical Data
#### Measure of Location
##### Mean
import numpy
x = list(range(0,11))
x.append(50)
numpy.mean(x)

##### Median
import numpy
x = list(range(0,11))
numpy.median(x)
5.0

##### Mode
from scipy import stats
x = [2,1,2,3,1,2,3,4,1,5,5,3,2,3]
stats.mode(x)[0][0]

#### Measure of Dispersion
##### Variance - Population
import numpy
x = [1, 2, 3]
numpy.var(x)

##### Variance - Sample
import numpy
x = [1, 2, 3]
numpy.var(x, ddof = 1) # ddof: Degree of freedom


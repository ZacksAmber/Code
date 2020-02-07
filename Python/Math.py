#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Title: math.py
# Created Date: February 04, 2020, 9:26:53 pm
# Author: Danlin Shen(shen.da@husky.neu.edu)
# Github: https://github.com/ZacksAmber/R
# Copyright (c) 2020 Danlin Shen
###

def exp(b, n):
    if n > 0:
        return b * exp(b, n - 1)
    else:
        return 1
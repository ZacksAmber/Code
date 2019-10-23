#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Title: Zacks.py
# Created Date: May 29, 2019, 7:21:34 pm
# Author: Danlin Shen(shen.da@husky.neu.edu)
# Github: https://github.com/ZacksAmber/R
# Copyright (c) 2019 Danlin Shen
###

# 次方 目前不能返回分数
def power(x, n=2):
    result = 1
    if n == 0:
        return result
    else:
        while n > 0:
            result *= x
            n -= 1
        while n < 0:
            result = 1/(result * x)
            n += 1
        return result

power(5,-2)



class check(x):
    def __init__(x):
        self.n = x
    def if_number(x):
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type for abs(): type(x)')
        else:
            return(x)

help(isinstance)


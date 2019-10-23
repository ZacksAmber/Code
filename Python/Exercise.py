#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Title: Exercise.py
# Created Date: May 24, 2019, 11:28:44 pm
# Author: Danlin Shen(shen.da@husky.neu.edu)
# Copyright (c) 2019 Danlin Shen
###

# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*n):
    result = 1
    for i in n:
        result = result * i
    return result
product(1, 2, 3)

66 + (6.23 * 65) + (12.7 * 168) - (6.8 * 25)


x = [0,21,32,1,23,3,4,4,2,3,-50]
sorted(x)

# 找出最小
"""
for i in x:
    if x[i] < x[i+1]:
        x.pop(i+1)
    print(x)
"""

Total Paid By Insurance
40,107
62,079
90,871
94,320
95,184
126,377

class number:
    def __init__(self, number):
        self.number = number
    def minimum(self, number):
        new_number = []
        self.number = number
        for i in number:
            if i > 0:
                #self.new_number.append(i)
                return number
        #return new_number


nx = number(x)
print(nx.minimum)
print(nx.number)

class Food: # Initializer
    '''Base class for foods.'''
    def __init__(self, name, cals):
        self.name = name
        self.cals = cals

    def change_name(self, name):
        self.name = name

    def change_cals(self, cals):
        self.cals = cals

class Fruit(Food): # dervied class
    pass

banana = Fruit("Banana", 100)
banana.change_cals(110)
print(banana.cals)

class Baked_good(Food): # dervied class
    ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

my_favorite = Baked_good("Brownie", 200)
my_favorite.add_ingredient("cocoa")
my_favorite.add_ingredient("egg")
print(my_favorite.ingredients)








def fib(n):
    if n == 1 or n == 2:
        return 1 # 注意是1, 不是n
    else:
        return fib(n-1) + fib(n-2)
fib(10)

def minimum(n):
    mean = sum(n)/len(n)
    new_n = [] # 再添加一个判断len(n) == 1的条件
    n_up = []
    n_down = []
    for i in n:
        if i >= mean:
            n_up.append(i)
        else:
            n_down.append(i)
    return(n_down + n_up)

minimum(x)
len(x)
x + x
print(x+x)

def find_min(n):
    for i in n:
        for j in n:


from math import *
def quadratic(a, b, c):
    x1 = -b + sqrt(b*b - 4*a*c)/(2*a)
    x2 = -b - sqrt(b*b - 4*a*c)/(2*a)
    if x1 == x2:
        return x1
    else:
        return x1, x2

quadratic(2, 3, 1)

print("Hello World")

n = 0
while n <= 5:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

l = ['a', 'c', 'b']
l.sort()
l

s = 'acb'
s.replace('a', 'A')
b = s.replace('a', 'A')
s
b

1.1 * 10000 / 352
900/28

# 分数
t9 = 14725
z = 8082/t9

# 2018 总人数: 16184
t8 = 16184

# 2017 总人数: 15402
t7 = 15402

# 2016 总人数: 16184
t6 = 16184

def filter_school (school = '学校', t2018 = 0, t2017 = 0):
    #return school
    #return t2018/t8
    #return t2017/t7
    print(f"学校: {school}\n2018排名: {t2018/t8}\n2018差值: {t2018/t8 - z}\n2017排名: {t2017/t7}\n2017差值: {t2017/t7 - z}\n")

filter_school("广东金融学院", 7169, 8124)
filter_school("上海体育学院", 7698)
filter_school("西南科技大学", 8237, 8064)
filter_school("西华大学", 8237, 8624)
filter_school("安徽建筑大学", 8703, 7765)
filter_school("河北金融学院", 8292, 7124)
filter_school("湖南财政经济学院", 9446, 7866)
filter_school("云南财经大学", 8703, 6571)
filter_school("陕西理工大学", 8367, 8195)
filter_school("山东交通学院", 7940, 7866)
filter_school("西南林业大学", 8703)
filter_school("大连交通大学", 8042, 7935)
filter_school("浙江农林大学", 7143, 7143)
filter_school("兰州理工", 8237, 8522)


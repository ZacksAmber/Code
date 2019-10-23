#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Title: Maical.py
# Created Date: May 25, 2019, 11:46:10 pm
# Author: Danlin Shen(shen.da@husky.neu.edu)
# Copyright (c) 2019 Danlin Shen
###

# 1. else 内部也可以嵌套条件.
temp = 0
raining = False
if temp > 10:
    print("warm")
else:
    if raining == True:
        print("It's raining")
    else:
        print("It's not raining")


# 2. break 可以被用于在一开始就中断循环; while 可以直接无条件开启循环.
num = 0
while True:
    if num == 5:
        break
    else:
        num += 1
    print(num)

# 3. loop 循环可以嵌套循环; 循环的statement可以取自其他循环.
for i in range(0, 2):
    for j in range(i, 3):
        print(j)

# 4. list 可以嵌套条件语句
a = [8, 4, 16, 20]
b = [x/2 for x in a]
print(b)

# 5. dictionary 字典中出现重复key时, 显示最后一个
d = {'a': 1, 'a': 0, 'b': 2}
print(d['a'])

# 6. [dictionary] 字典添加值的语法
d = {'a': 1, 'a': 0, 'b': 2}
d['c'] = 3
print(d)

# 7. interpolation 使用最简单易读的方式f-strings进行字符串调用
name = 'World'
program = 'Python'
print(f'Hello {name}! This is {program}!')

# 8. % 用于计算余数, 可以应用于日期计算中.
print(365 / 7)

# 9. docstring 可以快速了解某个函数的帮助文档.
help(print)
def birthday(name):
    '''Takes a string.
    Prints a birthday wish.'''
    print(f"happy birthday, {name}!")
help(birthday)
birthday("Amber")

def addtax(total, tax):
    '''Takes a bill total and tax.
    Returns the total with tax.'''
    return(total * (1 + tax))
help(addtax)
addtax(100, 0.07)

# 10. def 使用条件语句帮助函数debug.
def fun(x):
    '''Takes an int or float, adds two.'''
    if type(x) != int and type(x) != float:
        print("x must be a number!")
    else:
        return x + 2
fun("hi")
fun(3.14)

# 11. in 使用in来遍历字符串, 列表等.
def count_vowels(word):
    '''Returns the number of vowels in a string.'''
    count = 0
    for letter in word:
        if letter.lower() in "aeiou":
            count += 1
    return count
count_vowels("Amber")

# 12. iteration 迭代可以大幅度减少代码量, 比如计算阶乘.
def factorial_slow(n):
    if n == 1:
        return n
    else:
        result = 1
        for i in range(1, n):
            result *= (i+1)
        return result
factorial_slow(4)

def factorial(n):
    if n == 1: # base case
        return n
    else:      # recursive step
        return n * factorial(n - 1)
factorial(4)

# 13. Fibonacci 斐波那契尤其适合迭代.
# 1, 1, 2, 3, 5, 8 ...
def find_fib(n): # 如果不使用迭代, 将会使用大量变量.
    if n == 1 or n == 2:
        return 1 # 注意是1, 不是n
    else:
        counter = 3
        prev = 1
        curr = 1
        while counter <= n:
            temp = prev
            prev = curr
            curr = temp + prev
            counter += 1
        return curr
find_fib(4)

def fib(n):
    if n == 1 or n == 2:
        return 1 # 注意是1, 不是n
    else:
        return fib(n-1) + fib(n-2)
fib(4)

# 14. Palindrome 循环迭代.
def pal(str):
    if str.lower()[0] != str.lower()[-1]: # first != last
        return False
    else: # first is the same as last
        if len(str) == 1 or len(str) == 2:
            return True
        else:
            return pal(str[1:-1]) # 取字符串的range(1, -1)迭代.
pal("As453sa")
pal("Asbsa")

# 15. range 可以指定范围内的间隔; Python 使用:作为变量内的range
for i in range(0, 6, 2):
    print(i)

loves = "Zacks loves Amber."
loves[0:-1] == loves # False
loves[0:len(loves)] == loves # True
loves[-1] # -1 用来取最后一项, 但是别忘了range的形式是[)

# 16. class 基础形式, attributes, 和pass; mix of attributes
class Birthday:
    def __init__(self, day, month):
        self.day = day
        self.month = month
my_birthday = Birthday(25, "Febrary")
my_birthday # 显示内存位置
my_birthday.day
my_birthday.month

class Point:
    x = 0
    y = 0
    def __init__(self):
        z = 0
        pass
a = Point()
print(a.y)
a.x = 1 # 可以通过这种形式改变attribute的值
print(a.x)
print(a.z) # 但是不可以直接调用class函数内的值

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.awards = []
titanic = Movie("Titanic", 1997)
titanic.awards.append("Best Picture")
titanic.awards

# 17. Inheritance: derived class
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

""" Sample but error
class Baked_good(Food): # dervied class
    def __init__(self):
        Food.__init__(self)
        ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
"""

class Baked_good(Food): # dervied class
    ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

my_favorite = Baked_good("Brownie", 200)
my_favorite.add_ingredient("cocoa")
my_favorite.add_ingredient("egg")
print(my_favorite.ingredients)

# 18. class 灵活运用
class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Triangle(Shape):
    def find_area(self):
        return self.height * self.width / 2

class Rectangle(Shape):
    def find_area(self):
        return self.height * self.width

tri = Triangle(10, 10)
tri.find_area()

rec = Rectangle(10, 10)
rec.find_area()

# 19. Module
import math
math.sqrt(3)

import math as m
m.sqrt(3)

from math import sin, cos, pi # only use a few functions
sin(pi)

from math import * # use everything from a module
cos(pi) + sqrt(5)
help(sin)

import math, random # import multiple modules
my_number = random.randint(1, 10) # randint = random interger
my_number
math.sqrt(my_number)

from datetime import *
first = date(1994, 2, 25)
second = date(1999, 11, 10)
(first - second).days

# Arguments 可变参数, 传入0个及以上的参数, 并组装成tuple
def calc1 (n): # 非可变参数
    result = 0
    for i in n:
        result = result + i * i
    return result

calc1((1, 2, 3))
calc1([1, 2, 3])
calc1(1, 2, 3) # error 因为calc1 不是可变参数
calc1([])

def calc2 (*n): # 可变参数
    result = 0
    for i in n:
        result = result + i * i
    return result

calc2((1, 2, 3)) # error
calc2([1, 2, 3]) # error
calc2(1, 2, 3) # *n 是空的tuple, 传入1, 2, 3
calc2() # 甚至可以空值

# Arguments 关键字参数, 传入0个及以上的参数, 并组装成dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person("Amber", 19)
person('Zacks', 25, city='Beijing')

extra = {"city": "Beijing", "job": "Engineer"}
person("Zacks", 25, city = extra["city"], job = extra["job"]) # 复杂的输入
person("Zacks", 25, **extra) # 简单的输入, 获取dict所有内容

# Arguments 命名关键字参数 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456) # zipcode原本是不被认可的参数

def person(name, age, *, city, job): # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    print(name, age, city, job)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456) # error 拒绝未经许可的参数
person('Jack', 24, city='Beijing', job='Engineer')
person('Jack', 24, 'Beijing', 'Engineer') # error 命名参数必须传入参数名

def person(name, age, *, city='Beijing', job): # 通过设置缺省值, 简化函数
    print(name, age, city, job)
person("Zacks", 25, job = "job")

def person(name, age, *height, city = "Beijing", job): # 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
    print(name, age, height, city, job)
    print(type(height))
    print(type(name))
    print(type(city))
    print(type(job))
person("Zacks", 25, job = "job")
person("Zacks", 25, 168, job = "job")
type(person)

# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2, 3, 'a', 'b') # b没有传递给参数kw, 而是args
f1(1, 2, 3, 'a', 'b', x=99) # 写成dict的格式才能传递

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) # 通过tuple和dict调用f1
args = (1, 2, 3)
f2(*args, **kw) # 观察和f1的不同
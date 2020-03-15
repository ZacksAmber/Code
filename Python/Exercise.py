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

## List
l = [4, 5]
l.append(ll)
l.extend(ll)
l

l1 = [0, 1, 2]
l2 = [4, 5, 6]
l3 = l1 + l2
l3
# [0, 1, 2, 4, 5, 6]

l = [0, 1, 2]
l.append(l)
l


l2 = l1.copy()
l2
# [0, 1, 2, "list"]

# []

del l[-1]
l
# [0, 1, 2]

del l
l
# NameError: name 'l' is not defined

l.append(l[0])
l


t = (0, 1, 2, 3, l)
t.index(2)
# (0, 1, 2, 3, [4, 5])

l.append(6)
t
# (0, 1, 2, 3, [4, 5, 6])

ll = (0, 1, l)
ll


l = [0, 1, 2, "list"]
l[0:3]

t.append(4)

s = {0, 1, 2}
s
# {0, 1, 2}

s = {0, 1, 2}
s.add(4)
s
# {0, 1, 2, 4}

s.update([5, 6, 7])
s
# {0, 1, 2, 4, 5, 6, 7}

s1 = {0, 1, 2}
s2 = {4, 5, 6}
s3 = s1 + s2
s3 = s1.union(s2)
s3
# {0, 1, 2, 4, 5, 6}

t1 = (0, 1, 2)
t2 = (3, 4, 5)
t3 = t1 + t2
t3
# (0, 1, 2, 3, 4, 5)

s1.update(s2)
s1
# {0, 1, 2, 4, 5, 6}

t = (0, 1, 2)
del t
t
# NameError: name 't' is not defined

d = {
  "brand": "Ford",  "model": "Mustang",  "year": 1964
}

for x in d:
    print(x)
# brand
# model
# year

for b, n in d.items():
    print(b, n)
# brand Ford
# model Mustang
# Year 1964


s = set(("apple", "banana", "cherry")) # note the double round-brackets
s
# {'apple', 'banana',d = {
  "brand": "Ford",  "model": "Mustang",  "year": 1964
}
d.update({'brand': 'Ford', 'brand': 'Chevrolet'})
d
# {'brand': 'Chevrolet', 'model': 'Mustang', 'year': 1964}

d = {
  "brand": "Ford",  "model": "Mustang",  "year": 1964
}
d.update({'brand': 'Ford', 'brand': 'Chevrolet', 'year': 1964, 'year': 2020})
d
# {'brand': 'Chevrolet', 'model': 'Mustang', 'year': 2020}

x = float(1)
type(x)

ccp = """ The most crazy terrorist organization,which is no democracy, no freedom, and no human right.
It must be destroyed on 2020."""
print(ccp)
"""The most crazy terrorist organization,which is no democracy, no freedom, and no human right.
It must be destroyed on 2020."""

"Hello World!"[0:5]
# 'Hello'

"Hello World!"[-3:-1]
# 'ld'

(" Hello World!       ").strip()
# 'Hello World!'

(" Hello World!       ").lower()
# ' hello world!       '

(" Hello World!       ").upper()
# ' HELLO WORLD!       '

(" Hello World!       ").replace('H', 'A')
# ' Aello World!       '

(" Hello, World!").split(',')
# [' Hello', ' World!']

'!' in "Hello World!"
# True

'H' not in "Hello World!"
# False

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# I want to pay 49.95 dollars for 3 pieces of item 567.

a = 10
b = 10
result = ("{0} is greater than {1}")
if a > b:
    print(result.format(a, b))
elif a < b:
    print(result.format(b, a))
else:
    print("{0} is equal to {1}".format(a, b))
# 10 is equal to 10

a = 10
b = 10
result = ("{0} is greater than {1}")
if a > b:
    print(result.format(a, b))
else:
    print("{0} is not greater than {1}".format(a, b))
# 10 is not greater than 10

a = 10
b = 10
if a > b: print("{0} is greater than {1}".format(a, b))

t = 10
if t < 10:
    print("Temperature is {}. It is cold!".format(t))
    if t < 0:
        print("Temperature is {}. It is very cold!".format(t))
else:
    pass

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("This program is done")

"""
1
2
3
4
5
This program is done
"""

for i in [0, 1, 2]:
    print(i)
"""
0
1
2
"""

for i in range (3):
    print(i)
"""
0
1
2
"""

for i in range (2, 6):
    print(i)
"""
2
3
4
5
"""

for i in range (0, 3):
    print(i)
"""
0
1
2
"""

for i in "Fxxk CCP":
    print(i)
"""
F
x
x
k
 
C
C
P
"""

for i in range (0, 3):
    print(i)
    if i == 1:
        break
"""
0
1
"""

for i in range (0, 3):
    if i == 1:
        break
    else:
        print(i)
"""
0
"""

for i in range (0, 3):
    if i == 1:
        pass
    print(i)
"""
0
1
2
"""

for i in range (0, 3):
    if i == 1:
        pass
    else:
        print(i)
"""
0
2
"""

for i in range (0, 3):
    if i == 1:
        continue
    print(i)
"""
0
2
"""

for i in range (0, 3):
    if i == 1:
        continue
    else:
        print(i)
"""
0
2
"""

for i in range(1, 10, 3):
    print(i)
else:
    print("Finished")
"""
1
4
7
Finished
"""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(b, n)
"""
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""

len("Fxxk CCP")
# 8

print("Fxxk" + " CCP")
# Fxxk CCP

def my_function():
    print("Hello from a function")

my_function()
# Hello from a function

def hello_function(name):
    print("Hello " + name)

hello_function("Zacks")
# Hello Zacks
hello_function("Amber")
# Hello Amber
hello_function("33")
# Hello 33

# A function prints capitalized name
def name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    print("My name is " + first_name + " " + last_name)

name("Zacks", "Shen")
# My name is Zacks Shen

name("zacks", "SHEN")
# My name is Zacks Shen

name("Zacks")
# TypeError: name() missing 1 required positional argument: 'last_name'


# A function prints capitalized name
def _name(*name):
    name = list(name) # Remember 'tuple' object does not support item assignment
    index = len(name) # Get the length of 'name' argument
    for i in range(index):
        name[i] = name[i].capitalize()
    print("My name is " + name[0] + " " + name[1])

_name("Zacks", "Shen")
# My name is Zacks Shen

_name("zacks", "SHEN")
# My name is Zacks Shen

# A function prints capitalized name with a title
def name(first_name, last_name, title):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    title = title.upper()
    print("I am " + title + " " + first_name + " " + last_name)

name(title = "mr", last_name = "shen", first_name = "ZACKS")
# I am MR Zacks Shen

# A function prints capitalized name with a title
def _name(**name):
    name["first_name"] = name["first_name"].capitalize()
    name["last_name"] = name["last_name"].capitalize()
    name["title"] = name["title"].upper()
    print("I am " + name["title"] + " " + name["first_name"] + " " + name["last_name"])

_name(title = "mr", last_name = "shen", first_name = "ZACKS")
# I am MR Zacks Shen


# A function prints capitalized name with a title and country
def _name(country = "United States", **name): # Remember normal arg should put before **kwarg
    name["first_name"] = name["first_name"].capitalize()
    name["last_name"] = name["last_name"].capitalize()
    name["title"] = name["title"].upper()
    print("I am {0} {1} {2}, and I come from {3}".format(name["title"], name["first_name"], name["last_name"], country))

_name(title = "mr", last_name = "shen", first_name = "ZACKS")
# I am MR Zacks Shen, and I come from United States

_name(title = "mr", last_name = "shen", first_name = "ZACKS", country = "Iceland")
# I am MR Zacks Shen, and I come from Iceland
```


如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# A function prints capitalized name with a title and country
def name(first_name, last_name, title, *, country = "United States"):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    title = title.upper()
    print("I am {0} {1} {2}, and I come from {3}".format(title, first_name, last_name, country))

_name(title = "mr", last_name = "shen", first_name = "ZACKS")
# I am MR Zacks Shen, and I come from United States

_name(title = "mr", last_name = "shen", first_name = "ZACKS", country = "Iceland")
# I am MR Zacks Shen, and I come from Iceland

def name(first_name, last_name, title):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    title = title.upper()
    print("I am " + title + " " + first_name + " " + last_name)

name(title = "mr", last_name = "shen", first_name = "ZACKS")
# I am MR Zacks Shen

name(gender = "man", last_name = "shen", first_name = "ZACKS")

def _name(**name):
    name["first_name"] = name["first_name"].capitalize()
    name["last_name"] = name["last_name"].capitalize()
    name["title"] = name["title"].upper()
    print("I am {0} {1} {2}".format(name["title"], name["first_name"], name["last_name"]))

_name(title = "mr", last_name = "shen", first_name = "ZACKS")
# I am MR Zacks Shen

_name(gender = "man", last_name = "shen", first_name = "ZACKS")
# KeyError: 'title'

def _name(**name):
    name["first_name"] = name["first_name"].capitalize()
    name["last_name"] = name["last_name"].capitalize()
    name["title"] = name["title"].upper()
    print("I am {0} {1} {2}".format(name["title"], name["first_name"], name["last_name"]))

# A function prints capitalized name with a title and country
def name(first_name, last_name, title, *, country = "United States"):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    title = title.upper()
    print("I am {0} {1} {2}, and I come from {3}".format(title, first_name, last_name, country))

name(title = "mr", last_name = "shen", first_name = "ZACKS")
# I am MR Zacks Shen, and I come from United States

name(title = "mr", last_name = "shen", first_name = "ZACKS", country = "Iceland")
# I am MR Zacks Shen, and I come from Iceland

name(title = "mr", last_name = "shen", first_name = "ZACKS", gener = "Man")
# TypeError: name() got an unexpected keyword argument 'gener'


# A function prints capitalized name with a title and country
def name(first_name, last_name, *base_information, country = "United States"):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    print("I am {0} {1} {2}, a {3}, and I come from {4}".format(base_information[0].upper(), first_name, last_name, base_information[1], country))

name("Zacks", "shen", "mr", "man")
# I am MR Zacks Shen, and I come from United States

name("Zacks", "shen", "mr", "man", country = "Iceland")
# I am MR Zacks Shen, a man, and I come from Iceland

name(last_name = "shen", first_name = "Zacks", "mr", "man", country = "Iceland")
# SyntaxError: positional argument follows keyword argument
# Remember keyword argument must follows positional argument. Because I define last_name = "shen", which means the positional argument has been considered as keyword argument.

def name(first_name, last_name, *base_information, country = "United States"):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    print(base_information[0].upper())

name("Zacks", "shen", "mr", "man")

def _name(*name):
    name = list(name) # Remember 'tuple' object does not support item assignment
    index = len(name) # Get the length of 'name' argument
    for i in range(index):
        name[i] = name[i].capitalize()
    print("My name is " + name[0] + " " + name[1])

_name("Zacks", "Shen")
# My name is Zacks Shen

_name("zacks", "SHEN")
# My name is Zacks Shen

name = ("z", "a")
name[0]


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def bmi_calculate(h, w):
    return w/(h*h)

bmi_calculate(1.8, 70)
# 21.604938271604937

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")

tri_recursion(2)


# A function returns exponentiation
def exp(b, n):
    if n > 0:
        return b * exp(b, n - 1)
    else:
        return 1

# when n = 0, function returns exp(b, 0) -> 1
# when n = 1, function returns b * exp(b, 1) -> b * 1
# when n = 2, function retruns b * exp(b , n - 1) * exp(b , n - 2) -> b * b * 1

# Fibonacci number
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233…
0, 1, 2, 3, 4

# A function returns Fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib(6)

fib(12)
# 144


x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(2, 3))

def exp(b, n):
    if n > 0:
        return b * exp(b, n - 1)
    else:
        return 1

exp(2, 10)

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)

print(mydoubler(11))

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
cars[0] = "Toyota"

class MyClass:
    x = 5
    y = 6

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)
# 5
print(p1.y)
# 6

for i in [1, 2, 3, 4, 5]:
    print(i + "!")


a = [8, 4, 16, 20]
b = [x/2 for x in a]
print(b)
# [4.0, 2.0, 8.0, 10.0]


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
# John
print(p1.age)
# 36
print(p1)

x = 1
y = 5

while x:
    y -= 1

print(y)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Zacks", 25)

print(p1.name)
# Zacks
print(p1.age)
# 25
print(p1)
# <__main__.Person object at 0x1113db250>

p2 = Person()
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Zacks", 25)
p1.myfunc()
# Hello my name is Zacks

print(p1.name)
# Zacks
print(p1.age)
# 25
print(p1)
# <__main__.Person object at 0x1113db820>

######
class Exp:
    def __init__(self, b, n):
        self.b = b
        self.n = n

    if self.n >= 0:
        def Exp_1(self):
            if self.n > 0:
                return self.b * Exp_1(self.b, self.n - 1)
            else:
                return 1

Exp(2, 10)

######

class Person:
    def __init__(tmp, name, age):
        tmp.name = name
        tmp.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Zacks", 25)
p1.myfunc()
# Hello my name is Zacks

print(p1.name)
# 'Zacks'
print(p1.age)
# 25
print(p1)
# <__main__.Person object at 0x1124a4220>

p1.age = 18
print(p1.age)
# 18

del p1.age
print(p1.age)
# AttributeError: 'Person' object has no attribute 'age'
print(p1.name)
# Zacks

p2 = Person("Zacks", 25)
p2.name
print(p2.age)
p2.tmp()

del p1
print(p1)
# NameError: name 'p1' is not defined


class exp:
    def __init__(self, b, n):
        self.b = b
        self.n = n
        return self.b


    if self.n >= 0:
        def Exp_1(self):
            if self.n > 0:
                return self.b * Exp_1(self.b, self.n - 1)
            else:
                return 1


class exp:
    def __init__(self, b, n):
        self.b = b
        self.n = n

        if self.n >= 0:
            return self.b
        elif self.n < 0:
            return - self.b

p1 = exp(2, 10)
p1.b

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Zacks", 25)
print(p1.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        return("Hello my name is " + self.name)

    def unfinished_func(self):
        pass

p1 = Person("Zacks", 25)
p1.unfinished_func()
# AttributeError: 'Person' object has no attribute 'unfinished_func'

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def fullname(self):
        print("Hello, I'm {0} {1}".format(self.firstname, self.lastname))

#Use the Person class to create an object, and then execute the printname method:

x = Person("Zacks", "Shen")
x.fullname()
# Hello, I'm Zacks Shen

class Student(Person):
    pass

y = Student("Amber", "Lyu")
y.fullname()
# Hello, I'm Amber Lyu

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def fullname(self):
        print("Hello, I'm {0} {1}".format(self.firstname, self.lastname))

class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age



y = Student("Amber", "Lyu", 18)
y.fullname()
# Hello, I'm Amber Lyu
print(y.age)
# 18
print(y.fname)
# AttributeError: 'Student' object has no attribute 'fname'
print(y.lname)
# AttributeError: 'Student' object has no attribute 'lname'

class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age

    def fullname(self):
        print(self.age)

y = Student("Amber", "Lyu", 18)
y.fullname()
# 18




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Zacks", 25)

print(p1.name)
print(p1.age)
print(p1)



class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def fullname(self):
        print("Hello, I'm {0} {1}".format(self.firstname, self.lastname))

class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age

    def fullname(self):
        print("You did not invoke the parent class")

y = Student("Amber", "Lyu", 18)

print(y.age)
# 18
y.fullname()
# You did not invoke the parent class
print(y.firstname)
# Amber
print(y.lastname)
# Lyu

class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age

    def fullname(self):
        print(self.age)

y = Student("Amber", "Lyu", 18)
y.fullname()
# 18

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def fullname(self):
        print("Hello, I'm {0} {1}".format(self.firstname, self.lastname))

class Student(Person):
    pass

y = Student("Amber", "Lyu")

y.fullname()
# Hello, I'm Amber Lyu
print(y.firstname)
# Amber
print(y.lastname)
# Lyu



class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def fullname(self):
        print("Hello, I'm {0} {1}".format(self.firstname, self.lastname))

class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, ",", self.age, "years old,", "to the class.")

y = Student(age = 18, lname = "lyu", fname = "Amber")
y.welcome()

print(y.age)
# 18
y.fullname()
# Hello, I'm Amber lyu


l1 = [1, 2, 3]
for i in l1:
    print(i)
"""
1
2
3
"""


l = iter(l1)

print(next(l))
# 1
print(next(l))
# 2
print(next(l))
# 3
print(next(l))
# StopIteration: 

s1 = "GUNDAM"
for i in s1:
    print(i)
"""
G
U
N
D
A
M
"""

s = iter(s1)

print(next(s))
# G
print(next(s))
# U
print(next(s))
# N
print(next(s))
# D
print(next(s))
# A
print(next(s))
# M
print(next(s))
# StopIteration: 

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""
1
2
3
4
5
"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
"""
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
"""

class exp:
    def __init__(self, b, n):
        self.b = b
        self.n = n
    
    def exp_1(self):
        if self.n > 0:
            return self.b * exp_1(self, self.b, self.n)
        else:
            return 1

p1 = exp(2, 10)
print(p1.exp_1())
p1.exp_1()

def exp_1(b, n):
    if n > 0:
        return b * exp_1(b, n - 1)
    else:
        return 1

exp_1(2, 10)

class exp:
    def __init__(self, b, n):
        self.b = b
        self.n = n
        if self.n > 0:
            return self.b * __init__(self.b, self.n - 1)
        else:
            return 1

class exp:
    def __init__(self, b, n):
        self.b = b
        self.n = n
        if self.n == 0:
            print(1)
        if self.n > 0:
            def exp_1(self):
                    print(self.b * exp_1(self.b, self.n - 1))
        else:
            print(-self.b)

p1 = exp(2, 10)
print(p1.n)

del(i)
def loop(x):
    for i in range(x):
        print(i)

loop(3)
"""
0
1
2
"""

print(i)
# NameError: name 'i' is not defined

del(i)


def loop(x):
    x += 1
    for i in range(x):   
        def print_loop():
            print(i)
        print_loop() # execute print_loop()

loop(3)
"""
0
1
2
3
"""


x = 5

def myFunc():
    x = 10
    global x # You must assigned a global CHARiable before it has value
#   ^
# SyntaxError: name 'x' is assigned to before global declaration

x = 5

def myFunc():
    global x
    x = 10

myFunc()
print(x)

myFunc()
# 10
print(x)
# 5

def exp(b, n):
    if n > 0:
        return b * exp(b, n - 1)
    else:
        return 1

exp(2, 10)


import Math
Math.exp(2, 10)
# 1024

from Math import exp
exp(2, 10)
# 1024

person = {
    "Name": "Zacks",    "Age": 25,    "Country": "United States"
}

import tmp as population
print(population.person)
# {'Name': 'Zacks', 'Age': 25, 'Country': 'United States'}

from tmp import person
print(person)
# {'Name': 'Zacks', 'Age': 25, 'Country': 'United States'}
print(person["Name"])
# Zacks

import Math
dir(Math)
"""
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'exp']
"""

import tmp
dir(tmp)
"""
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'person']
"""

import platform
dir(platform)
"""
['_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture', '_follow_symlinks', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_mac_ver_xml', '_node', '_norm_version', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', '_ver_output', '_ver_stages', 'architecture', 'collections', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']
"""

import sys
sys.path
"""
['/private/CHAR/folders/31/lj6nmqhx1711vgv7r7g9r_cm0000gp/T/9c5d056e-aad5-4997-99e9-b8991b740258', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', '', '/Users/zack/Library/Python/3.8/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages', '/Users/zack/Library/Python/3.8/lib/python/site-packages/IPython/extensions', '/Users/zack/.ipython']
 """

import platform
print(platform.python_version())
# 3.8.1

import sys
sys.path
"""
['/private/CHAR/folders/31/lj6nmqhx1711vgv7r7g9r_cm0000gp/T/c1b404a3-2753-4a56-931a-20c02831e04f', '/Users/zack/.vscode/extensions/ms-python.python-2020.1.58038/pythonFiles', '/Users/zack/.vscode/extensions/ms-python.python-2020.1.58038/pythonFiles/lib/python', '/Users/zack/opt/anaconda3/lib/python37.zip', '/Users/zack/opt/anaconda3/lib/python3.7', '/Users/zack/opt/anaconda3/lib/python3.7/lib-dynload', '', '/Users/zack/opt/anaconda3/lib/python3.7/site-packages', '/Users/zack/opt/anaconda3/lib/python3.7/site-packages/aeosa', '/Users/zack/opt/anaconda3/lib/python3.7/site-packages/IPython/extensions', '/Users/zack/.ipython']
"""

import sys
sys.path.append("/tmp")
sys.path
"""
['/private/CHAR/folders/31/lj6nmqhx1711vgv7r7g9r_cm0000gp/T/c1b404a3-2753-4a56-931a-20c02831e04f', '/Users/zack/.vscode/extensions/ms-python.python-2020.1.58038/pythonFiles', '/Users/zack/.vscode/extensions/ms-python.python-2020.1.58038/pythonFiles/lib/python', '/Users/zack/opt/anaconda3/lib/python37.zip', '/Users/zack/opt/anaconda3/lib/python3.7', '/Users/zack/opt/anaconda3/lib/python3.7/lib-dynload', '', '/Users/zack/opt/anaconda3/lib/python3.7/site-packages', '/Users/zack/opt/anaconda3/lib/python3.7/site-packages/aeosa', '/Users/zack/opt/anaconda3/lib/python3.7/site-packages/IPython/extensions', '/Users/zack/.ipython', '/tmp']
"""

import datetime
dir(datetime)
"""
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
 """

import datetime
datetime.datetime.now()
# datetime.datetime(2020, 2, 5, 15, 33, 8, 732931)

import datetime
t = datetime.datetime.now()
print(t. year)
# 2020
print(t.strftime("%A"))
# Wednesday
print(t.strftime())

Kobe_Bryant = datetime.datetime(2020, 1, 26)
print(Kobe_Bryant)
# 2020-01-26 00:00:00
print(Kobe_Bryant.day)
# 26
print(Kobe_Bryant.strftime("%B"))

help(datetime.datetime)
"""
class datetime(date)
 |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
 ...
"""

Kobe_Bryant = datetime.datetime(2020, 1, 26, 15, 50, 23)
Kobe_Bryant.isoformat()
# '2020-01-26T15:50:23'
Kobe_Bryant.ctime()
# 'Sun Jan 26 15:50:23 2020'
print(Kobe_Bryant.strftime("%B"))
"January"


import json

# Create a dict named data; data has one key.
data = {}
data['people'] = []

# Add three values to the key people.
data['people'].append({
    'name': 'Scott',    'website': 'stackabuse.com',    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',    'website': 'google.com',    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',    'website': 'apple.com',    'from': 'Alabama'
})

# Save data to the file named sample.json. It will be saved to the same working directory as your current Python working directory.
with open('sample.json', 'w') as output_file:
    json.dump(data, output_file)
# {'people': [{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}, {'name': 'Larry', 'website': 'google.com', 'from': 'Michigan'}, {'name': 'Tim', 'website': 'apple.com', 'from': 'Alabama'}]}

import json

with open('sample.json') as json_file:
    data = json.load(json_file)
    for i in data['people']:
        print('Name: ' + i['name'])
        print('Website: ' + i['website'])
        print('From: ' + i['from'])
        print('')
"""
Name: Scott
Website: stackabuse.com
From: Nebraska

Name: Larry
Website: google.com
From: Michigan

Name: Tim
Website: apple.com
From: Alabama
"""

import json

# a Python object (dict):
x = {
    "name": "John",    "age": 30,    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
# {"name": "John", "age": 30, "city": "New York"}
type(x)
# dict
type(y)
# str

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
"""
{"name": "John", "age": 30}
["apple", "bananas"]
["apple", "bananas"]
"hello"
42
31.76
true
false
null
"""

import json

x = {
    "name": "John",    "age": 30,    "married": True,    "divorced": False,    "children": ("Ann","Billy"),    "pets": None,    "cars": [
        {"model": "BMW 230", "mpg": 27.5},        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
# {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

json.dumps(x, indent=4, separators=(". ", "= "))
"""
{
    "name" = "John".
    "age" = 30.
    "married" = true.
    "divorced" = false.
    "children" = [
        "Ann".
        "Billy"
    ],    "pets" = null.
    "cars" = [
        {
            "model" = "BMW 230".
            "mpg" = 27.5
        }.
        {
            "model" = "Ford Edge".
            "mpg" = 24.1
        }
    ]
}
"""

json.dumps(x, indent=4, sort_keys=True)
"""
{
    "age": 30,    "cars": [
        {
            "model": "BMW 230",            "mpg": 27.5
        },        {
            "model": "Ford Edge",            "mpg": 24.1
        }
    ],    "children": [
        "Ann",        "Billy"
    ],    "divorced": false,    "married": true,    "name": "John",    "pets": null
}
"""

import camelcase

c = camelcase.CamelCase() # #This method capitalizes the first letter of each word.
txt = "hello world"
print(c.hump(txt))
# Hello World


import mysql.connector

root_db = mysql.connector.connect(
    host='localhost',    user='root',    password='00GUNDAM7Sword/GM',    auth_plugin='mysql_native_password'
)

mysql_root = mysql.connector.connect(
    host='localhost',    user='root',    passwd='00GUNDAM7Sword/GM'
)

import mysql.connector

root_db = mysql.connector.connect(
    host='localhost',    user='root',    password='password'



import mysql.connector

mysql_root = mysql.connector.connect(
    host="localhost",    user="your_username",    passwd="your_password"
)

root_cursor = mysql_root.cursor()

root_cursor.execute("CREATE DATABASE mydatabase")

root_cursor.execute("CREATE USER 'test'@'localhost' \
    IDENTIFIED WITH caching_sha2_password BY 'passwd' \
    PASSWORD EXPIRE INTERVAL 30 DAY \
    FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;")

import mysql.connector

mysql_test = mysql.connector.connect(
    host="localhost",    user="test",    passwd="passwd"
)

import urllib2
url = 'https://data.boston.gov/api/3/action/datastore_search?resource_id=ea2e4696-4a2d-429c-9807-d02eb92e0222&limit=5&q=title:jones'  
fileobj = urllib.urlopen(url)
print fileobj.read()

###############

> [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
> [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

import pandas

bos311 = pandas.read_csv('tmpr2k_j017.csv')
bos311.columns


bos311.dtypes

import pandas

bos311 = pandas.read_csv('tmpr2k_j017.csv')
bos311.head(10)


import mysql.connector

mysql_test = mysql.connector.connect(
    host="localhost",    user="test",    passwd="passwd",    database="BOS311"
)

test_cursor = mysql_test.cursor()
test_cursor.execute("USE BOS311;")
test_cursor.execute("SELECT * FROM test LIMIT 10;")

for row in test_cursor:
    print(row)


cloud-analytics-db.crmnbmzm85lc.us-east-1.rds.amazonaws.com

admin
Test1234

import mysql.connector

mysql_test = mysql.connector.connect(
    host="cloud-analytics-db.crmnbmzm85lc.us-east-1.rds.amazonaws.com",    user="admin",    passwd="Test1234",    database="bosbot"
)

test_cursor = mysql_test.cursor()

###

from flask import Flask
app = Flask(_name_)

@app.route('/findDuplicate')
def hello_world():

    return "Hello World"

if _name_ == '_main_':
   app.run()

####

test_cursor = test.cursor()

test_cursor.execute("USE bosbot;")

test_cursor.execute("select * from 311_sample;")

for row in test_cursor:
    print(row)

#######
Select <列的集合> from <表名> where <条件> order by <排序字段和方式>

test_cursor.execute("SELECT reason FROM test LIMIT 10;")

SELECT * FROM test WHERE reason LIMIT 10;
SELECT * FROM test LIMIT 10;

SELECT * FROM test WHERE reason='Trees';


test_cursor.execute("SELECT * FROM test WHERE reason='Trees' LIMIT 2;")

tmp = []
for row in test_cursor:
    tmp.append(row)
    type(row)

tmp

101003176264 in tmp[1]

type(row)

test_cursor.execute("SELECT COUNT(*) as repetitions, reason FROM test GROUP BY reason WHERE HAVING repetitions > 1 ORDER BY repetitions DESC;")

for row in test_cursor:
    print(row)


SELECT COUNT(*) as repetitions, reason FROM test GROUP BY reason WHERE location_street_name='8 Clover St' HAVING repetitions > 1 ORDER BY repetitions DESC;


SELECT * from test WHERE location_zipcode='02122';
SELECT * from test WHERE location_street_name='8 Clover St';

import mysql.connector

mysql_test = mysql.connector.connect(
    host="localhost",    user="test",    passwd="passwd",    database="BOS311"
)

test_cursor = mysql_test.cursor()
test_cursor.execute("SELECT * FROM test")
result = test_cursor.fetchall()

type(result)
# list
type(result[0])
# tuple

result[0]





import mysql.connector

mysql_test = mysql.connector.connect(
    host="localhost",    user="test",    passwd="passwd",    database="BOS311"
)

test_cursor = mysql_test.cursor()

sql = "SELECT * FROM test WHERE location_zipcode='02155'"

test_cursor.execute(sql)

result = test_cursor.fetchall()



def judge_duplicated():
    sql = "SELECT * FROM test WHERE reason = '{0}' AND location_zipcode = '{1}' AND '{2}'".format(
    case_information['reason'],    case_information['location_zipcode'],    case_information['location_street_name']
)

    test_cursor.execute(sql)
    result = test_cursor.fetchall()
    return(len(result))

judge_duplicated()

def t(x = input('s')):
    print(x)


SELECT * FROM test WHERE open_dt LIKE "2020-01-22%" AND location_zipcode = "02203";

SELECT * FROM test WHERE location_zipcode = "02203" AND open_dt LIKE "2020-01-22%";

def judge_date():
    sql = "SELECT * FROM test WHERE reason = '{0}' AND location_zipcode = '{1}' AND '{2}' AND case_status = '{3}' AND open_dt LIKE '{4}%'".format(
        case_information['reason'],        case_information['location_zipcode'],        case_information['location_street_name'],        case_information['case_status'],        case_information['open_dt']
    )

    test_cursor.execute(sql)
    result = test_cursor.fetchall()
    return(result)

judge_date()

sql

SELECT * FROM test WHERE reason = 'Street Lights' AND location_zipcode = '02203' AND '15 Sudbury St' AND case_status = 'Open' AND open_dt LIKE '2020-01-22%'

case_information['open_dt'] == "2020-01-31"





if judge_date():
    print("Y")
else:
    print("N")

if judge_duplicated():
    print("Y")
else:
    print("N")

judge_date() and case_information['open_dt'] == "2020-01-31"

case_information

def judge_date():
    sql = "SELECT * FROM test WHERE reason = '{0}' AND location_zipcode = '{1}' AND '{2}' AND case_status = '{3}' AND open_dt LIKE '{4}%'".format(
        case_information['reason'],        case_information['location_zipcode'],        case_information['location_street_name'],        case_information['case_status'],        case_information['open_dt']
    )

    test_cursor.execute(sql)
    result = test_cursor.fetchall()
    return(result)

git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch /Python/311_service_requests_2019.csv' HEAD

bfg --delete-files 311_service_requests_2019.csv

git filter-branch --index-filter 'git rm -r --cached --ignore-unmatch 311_service_requests_2019.csv' HEAD

git rm --cached 311_service_requests_2019.csv

git reset --soft HEAD~7


import mysql.connector

mysql_test = mysql.connector.connect(
    host="cloud-analytics-db.crmnbmzm85lc.us-east-1.rds.amazonaws.com",    user="admin",    passwd="Test1234",    database="bosbot"
)


from flask import Flask
app = Flask(_name_)

@app.route('/findDuplicate')
def hello_world():

    return "Hello World"

if _name_ == '_main_':
   app.run()


def judge_date():
    sql = "SELECT * FROM test WHERE reason = '{0}' AND location_zipcode = '{1}' AND '{2}' AND case_status = '{3}' AND open_dt LIKE '{4}%'".format(
        case_information['reason'],        case_information['location_zipcode'],        case_information['location_street_name'],        case_information['case_status'],        case_information['open_dt']
    )

    test_cursor.execute(sql)
    result = test_cursor.fetchall()
    return result

# comment



def exp(b, n):
    b = int(b)
    n = int(n)
    if n == 0:
        return 1
    elif n == 1:
        return b
    elif n >= 2:
        return exp1(b, n)
    else:
        return exp2(b, -n)

def exp1(b, n):
    if n >= 2:
        return b * exp1(b, n-1)
    else:
        return b

def exp2(b, n):
    if n >= 2:
        return b * exp2(b, n-1)
    else:
        return b

def exp3(b):
    return(b)

def t():
    for i in range(3):
        return(i)

t()

exp(2, -10)

def exp(b, n):
    if n >= 1:
        return b * exp(b, n - 1)
    else:
        return 1


def exp(b, n):
    if n >= 2:
        return b * exp(b, n - 1)
    else:
        print(b)

exp(3, 3)

2 ** 10

-10 ** 1

-1/27

for i in range(3):
    print(i)


def tmp():
    for i in range(3):
        print(i)

tmp()

def bmi_calculate_1(h, w):
    return w/(h*h)

bmi_calculate_1(1.8, 70)
# 21.604938271604937

def bmi_calculate_2(h, w):
    print( w/(h*h))

bmi_calculate_2(1.8, 70)
# 21.604938271604937


# A function try to RETURN the values in a range one by one, but it doesn't work.
def tmp():
    for i in range(3):
        return(i)

tmp()


def hello_1():
    print("Hello")
    print("World")

hello_1()
# Hello
# World

def hello_2():
    return("Hello")
    return("World") # Will be ignored!

hello_2()
# 'Hello'

def hello_3():
    return("Hello")
    print("World") # Will be ignored!

hello_3()
# 'Hello'

def hello_4():
    print("Hello")
    return("World") # Will not be ignored!

hello_4()
# Hello
# 'World'


def while_loop_1(i):
    while i < 5:
        return i
        i += 1

while_loop_1(1)
# 1

def while_loop_2(i):
    while i < 5:
        print(i)
        i += 1

while_loop_2(1)
# 1
# 2
# 3
# 4

def while_loop_3(i):
    while i < 5:
        l = i
        i += 1

while_loop_2(1)


def tmp_2():
    for i in range(3):
        return(i)

import plotly.express as px
print(px.data.iris.__doc__)
px.data.iris().head()

print("hello world")

import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()

import plotly.graph_objects as go
fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()

import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="rug", marginal_x="histogram")
fig

import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200) - 1
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 1

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = ['#333F44', '#37AA9C', '#94F3E4']

# Create distplot with curve_type set to 'normal'
fig = ff.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)

# Add title
fig.update_layout(title_text='Curve and Rug Plot')
fig.show()




import pandas as pd
import numpy as np
import plotly.express as px

# Define Wight
np.random.seed(1234)
weight1 = np.random.normal(55, size = 200)
weight2 = np.random.normal(58, size = 200)
weight = np.append(weight1, weight2)

# Define sex
sex = ['F'] * 200 + ['M'] * 200

# Define Data Frame
wdata = pd.DataFrame(list(zip(sex, weight)), columns = ["Sex", "Weight"]) # zip() for zipping two lists


w1 = wdata[wdata['Sex'] == 'F'].iloc[:, 1]
w2 = wdata[wdata['Sex'] == 'M'].iloc[:, 1]


wdata[wdata['Sex'] == 'M']

df[df.p1.isin(['SD','HN'])]

import mysql.connector

mysql_root = mysql.connector.connect(
    host="localhost",    user="test",    passwd="passwd"
)

mysql_root = mysql.connector.connect(
    host="localhost",    user="root",    passwd="00GUNDAM7Sword/GM"
)


sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}' AND open_dt LIKE '%{3}%'".format(
    mysql_table,    case_information['reason'],    case_information['location'],    case_information['open_dt']
)

mysql.execute(sql)
result = mysql.fetchall()

result[0][1].strftime("%Y-%m-%d %H:%M:%S")[0:10]

def mysql_UPDATE_case_status(case_status):
    case_information['case_status'] = case_status

    sql = "UPDATE {0} SET case_status = {1} WHERE reason = '{2}' AND location = '{3}'".format(
        mysql_table,        case_information['case_status'],        case_information['reason'],        case_information['location']
    )

    mysql.execute(sql)
    mysql_connect.commit()
    print(mysql.rowcount, "record(s) affected")

sql = "UPDATE {0} SET case_status = '{1}' WHERE reason = '{2}' AND location = '{3}'".format(
    mysql_table,    case_information['case_status'],    case_information['reason'],    case_information['location']
)

case_information = {}
case_information['location'] = "87 Blue Hill Ave  Roxbury  MA  02119"
case_information['reason'] = "Housing"


SELECT * FROM sample_311 WHERE reason = 'Housing' AND location = '87 Blue Hill Ave  Roxbury  MA  02119';

sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
    mysql_table,    case_information['reason'],    case_information['location']
)

mysql.execute(sql)
result = mysql.fetchall()

result[0][-1]

l = []
for i in result:
    if i[5] == 'Open':
        l.append(i)
len(l)

if datetime.datetime.now().date().isoformat() in l:
    return(result)
else:
    return(None) 

l = [1, 2, 3]
max(l)

class MyClass:
    x = 5
    y = 6


MyClass().x
MyClass().y
MyClass().z

def d_Person(name, age):
    name = name
    age = age

# Create a Class named Person:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        return("Hello my name is " + self.name)

p1 = Person("Zacks", 25)

def Weather(location):
    weather = "Sunny"
    Summary = "{0}: Today is {1}".format(location, weather)
    return(Summary)

Weather("Boston")
# 'Boston: Today is Sunny'

# Provide weather information based on location
def Weather(location):
    weather = "Sunny" # Assume you have gotten the weather from somewhere.
    humidity = "20%"
    Summary = "{0}: Today is {1}, and humidity is {2}".format(location, weather, humidity)
    return(Summary)

Weather("Boston")
# 'Boston: Today is Sunny, and humidity is 20%'


import datetime

class Weather:
    def __init__(self, location):
        self.location = location

    def Date(self, date = 0):
        self.date = datetime.date.today() + datetime.timedelta(days = date)
        print("Date: " + self.date.isoformat())

    def Location(self):
        print("Location: " + self.location)
        
    def Weather(self):
        self.weather = "Sunny"
        print("Weather: " + self.weather)

    def Humidity(self):
        self.humidity = "20%"
        print("Humidity: " + self.humidity)

    def Rain(self):
        self.rain = "10%"
        print("Chance of Rain: " + self.rain)

    def Summary(self): # Invoke all functions above
        for i in range (6):
            self.Date(i)
            self.Location()
            self.Weather()
            self.Humidity()
            self.Rain()
            print("")

location_1 = Weather("Boston")
location_1.Summary()

"""
Date: 2020-02-26
Location: Boston
Weather: Sunny
Humidity: 20%
Chance of Rain: 10%

Date: 2020-02-27
Location: Boston
Weather: Sunny
Humidity: 20%
Chance of Rain: 10%

Date: 2020-02-28
Location: Boston
Weather: Sunny
Humidity: 20%
Chance of Rain: 10%

Date: 2020-02-29
Location: Boston
Weather: Sunny
Humidity: 20%
Chance of Rain: 10%

Date: 2020-03-01
Location: Boston
Weather: Sunny
Humidity: 20%
Chance of Rain: 10%
"""


# import required modules 
import requests, json 
  
# Enter your API key here 
api_key = "af239eac3d426ff8aa48238038f3e701"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/forecast"

# Give Location 
location = input("Enter Location : ") 

# complete_url variable to store 
# complete url address 
complete_url = base_url + "?q=" + location + "&appid=" + api_key

# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 

x

x['list'][0] # date 0


# kelvin unit
int(x['list'][0]['main']['temp'] - 273.15)
int(x['list'][0]['main']['temp_min'] - 273.15)
int(x['list'][0]['main']['temp_max'] - 273.15)

# Weather
x['list'][0]['weather'][0]['main'] 

# Humidity
x['list'][0]['main']['humidity']

# Chance of Rain
x['list'][0]

self.x['list'][date]['rain']['3h']

x['list'][0s]

import datetime
import requests, json

class Weather:
    def __init__(self, location):
        self.location = location

    def API(self):
        # Enter your API key here 
        api_key = "af239eac3d426ff8aa48238038f3e701"

        # base_url variable to store url 
        base_url = "http://api.openweathermap.org/data/2.5/forecast"

        # complete_url variable to store 
        # complete url address 
        #complete_url = base_url + "?q=" + self.location + "&appid=" + api_key
        complete_url = base_url + "?zip=" + self.location + "&appid=" + api_key

        # get method of requests module 
        # return response object 
        response = requests.get(complete_url)

        # json method of response object  
        # convert json format data into 
        # python format data 
        self.x = response.json()

    def Date(self, date = 0):
        self.date = datetime.date.today() + datetime.timedelta(days = date)
        print("Date: " + self.date.isoformat())

    def Location(self):
        print("Location: " + self.location)
        
    def Temperature(self, date = 0):
        # - kelvin unit (273.15)
        self.temp = int(self.x['list'][date]['main']['temp'] - 273.15)
        self.temp_min = int(self.x['list'][date]['main']['temp_min'] - 273.15)
        self.temp_max = int(self.x['list'][date]['main']['temp_max'] - 273.15)

        print("Temperature: " + str(self.temp) + "°C")
        print("Min temperature: " + str(self.temp_min) + "°C")
        print("Max temperature: " + str(self.temp_max) + "°C")
    def Weather(self, date = 0):
        self.weather = self.x['list'][date]['weather'][0]['main']
        
        print("Weather: " + self.weather)

    def Humidity(self, date = 0):
        self.humidity = self.x['list'][date]['main']['humidity']

        print("Humidity: " + str(self.humidity) + "%")

    """ Give up because miss information
    def Rain(self, date = 0):
        self.rain = self.x['list'][date]['rain']['3h']

        print("Chance of Rain: " + self.rain)
    """

    def Summary(self): # Invoke all functions above
        self.API()

        for i in range (6):
            self.Date(i)
            self.Location()
            self.Weather(i)
            self.Temperature(i)
            self.Humidity(i)
    #        self.Rain(i)
            print("")

#location = Weather(input("Input Your Location: "))
print("Sample 'Zip Code, Country Code': 02115, us")
location = Weather(input("Input Your 'Zip Code, Country Code': "))
location.Summary()


import plotly.express as px

dir(px.data)


import plotly.express as px

df = px.data.gapminder()
fig = px.scatter(df, x = "gdpPercap", y = "lifeExp", animation_frame = "year", animation_group = "country",           size="pop", color = "continent", hover_name = "country", facet_col = "continent",           log_x = True, size_max = 45, range_x = [100,100000], range_y = [25,90])
fig.show()

people <- list(name = c("John", "Joe"), grades = c(99, 98), athlete = c(TRUE, FALSE))

people = {"name": ["John", "Joe"], "grades": [99, 98], "athlete": [True, False]}

people["name"][0]

name = ["John", "Joe"]
grades = [99, 98]
athlete = [True, False]

people = [name, grades, athlete]

people


SELECT * FROM indicator_data WHERE score != 10 AND classification != 'TP/DE' ORDER BY score \G


SELECT * FROM indicator_data WHERE alter_category = 'Atomic' \G

dir(px.colors)

data = pd.read_csv('https://raw.githubusercontent.com/drazenz/heatmap/master/autos.clean.csv')

corr = data.corr()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,    cmap=sns.diverging_palette(20, 220, n=200),    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),    rotation=45,    horizontalalignment='right'
);

2.14 - 2.29 586
3.1 - 1.31 1000
4.1 - 4.30
5.1 - 5.31
6.1 - 6.30
7.1 - 7.20


-994.88 + 240.22 + 5463.78 + 2048.64 + 315.18 - 1900.06

cost = 400 * 67.8 + 800 * 67.3425 + 50 * 66.35

income = 75.75 * 650 + 76.47 * 600

income - cost

100 * 1.1 ** 7

l = [0, 1, 2, 3]
l[2:] = 4, 5, 6, 8, 9 ,10

l
# [0, 1, 4, 5, 6, 8, 9, 10]

l = [0, 1, 2, 3]
l = l + [4]

l
# [0, 1, 2, 3, 4]

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

del(areas[-4:-2])

areas


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = areas.copy()

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
# [11.25, 18.0, 20.0, 10.75, 9.5]

help(complex())
?complex()

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
areas.index(20.0)

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))


import math
math.pi

math.pi ** 2

math.pi * math.pi

math.radians(360)

help(math.radians)


height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

height * weight
# TypeError: can't multiply sequence by non-int of type 'list'

h_w = [round(height[i] * weight[i], 3) for i in range(len(height))]

h_w
# [113.142, 99.456, 108.756, 167.076, 122.973]


h_w = []
for i in range(len(height)):
    h_w.append(round(height[i] * weight[i], 3))

print(h_w)
# [113.14, 99.46, 108.76, 167.08, 122.97]

import numpy as np

height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

print(height * weight)
# [113.142  99.456 108.756 167.076 122.973]

np.zeros(2)
array([0., 0.])

import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

print(a)
# [[1 2 3]
# [4 5 6]
# [7 8 9]]

a
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

a = np.array([2, 1, 5, 3, 7, 4, 6, 8])

np.sort(a)
# array([1, 2, 3, 4, 5, 6, 7, 8])

a = np.array([2, 1, 5, 3, 7, 4, 6, 8])

np.sort(-a)
# 


height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 50.0, 69.6, 88.4, 68.7]
values = [(height[i], weight[i]) for i in range(len(height))]

dtype = [('height', float), ('weight', float)]
h_w = np.array(values, dtype = dtype)

h_w
# array([(1.73, 65.4), (1.68, 50. ), (1.71, 69.6), (1.89, 88.4),
#        (1.79, 68.7)], dtype=[('height', '<f8'), ('weight', '<f8')])

np.sort(h_w, order = 'height')
# array([(1.68, 50. ), (1.71, 69.6), (1.73, 65.4), (1.79, 68.7),
#        (1.89, 88.4)], dtype=[('height', '<f8'), ('weight', '<f8')])

np.sort(h_w, order = 'weight')
# array([(1.68, 50. ), (1.73, 65.4), (1.79, 68.7), (1.71, 69.6),
#        (1.89, 88.4)], dtype=[('height', '<f8'), ('weight', '<f8')])

np.sort(h_w, order = 'height') == np.sort(h_w, axis = -1)
# array([ True,  True,  True,  True,  True])

np.sort(h_w, order = 'weight') == np.sort(h_w, axis = 1)
# 

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))
# array([1, 2, 3, 4, 5, 6, 7, 8])


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
np.concatenate((x, y), axis = 0)
# array([[1, 2],
#       [3, 4],
#       [5, 6],
#       [7, 8]])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
np.concatenate((x, y), axis = 1)
# array([[1, 2, 5, 6],
#        [3, 4, 7, 8]])

# List
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

a + b
# [1, 2, 3, 4, 5, 6, 7, 8]

# ndarray
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

a + b
# array([ 6,  8, 10, 12])


import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
bmi = np.around(bmi, 3)

bmi
# array([21.852, 20.975, 21.75 , 24.747, 21.441])

bmi > 24
# array([False, False, False,  True, False])

bmi[bmi > 24]
# array([24.747])

l = [1, 2, 3]
l * 3

x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]

import numpy as np

l = [1, 2, 3]

print(l)
# [1, 2, 3]

import numpy as np

a = np.array([1, 2, 3])

a.shape
# (3,)
np.sum(a, axis = 0)
# 6

a[0]
# 1
a[1]
# 2
a[2]
# 3

print(a)
# [1 2 3]
a
# array([1, 2, 3])

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

a.shape
# (2, 3)
a
# array([[1, 2, 3],
#        [4, 5, 6]])

np.sum(a, axis = 0) # the sum of the array by row
# array([5, 7, 9])
np.sum(a, axis = 1) # the sum of the array by column
# array([ 6, 15])

a[0] # the first row
# array([1, 2, 3])
a[1] # the second row
# array([4, 5, 6])

a[0][0] # the element of the first row and the first column
# 1
a[1][2] # the element of the second row and the third column
# 6
a[-1][-1] # the element of the last row and the last column
# 6


import numpy as np

a = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]],
             [[8, 9, 10, 11], [12, 13, 14, 15]]])


a.shape
# (2, 2, 4)
a[0] # axis = 0
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7]])
a[1] # axis = 1
# array([[ 8,  9, 10, 11],
#        [12, 13, 14, 15]])

a[0][0] #
# array([0, 1, 2, 3])
a[0][1]
# array([4, 5, 6, 7])
a[1][0]
# array([ 8,  9, 10, 11])
a[1][1]
# array([12, 13, 14, 15])

a[0][0][0]
# 0
a[0][0][1]
# 1
a[-1][-1][-1]
# 15

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

n_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]])
n_2d.shape # 2 rows, 5 columns

np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat

import numpy as np

a = np.array([1, 2, 3])

a[0]
# 1
a[-1]
# 3
a[0:2]
# array([1, 2])
a[1:]
# array([2, 3])
a[:-2]
# array([1])
import numpy as np
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

a
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15]])

a.shape # 4 rows, 4 columns
# (4, 4)

a < 5
# array([[ True,  True,  True,  True],
#        [ True, False, False, False],
#        [False, False, False, False],
#        [False, False, False, False]])

a[a < 5]
# array([0, 1, 2, 3, 4])

a[a >= 5]
# array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

a[a%2 == 0]
# array([ 0,  2,  4,  6,  8, 10, 12, 14])

b = a[(a > 5) | (a == 5)]
b
# array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])

c = a[(a > 2) & (a < 11)]
c
# array([ 3,  4,  5,  6,  7,  8,  9, 10])

d = np.nonzero(a < 5)
d # row + column
# (array([0, 0, 0, 0, 1]), array([0, 1, 2, 3, 0]))


list_of_coordinates = list(zip(d[0], d[1]))

for coord in list_of_coordinates:
    print(coord)
# (0, 0)
# (0, 1)
# (0, 2)
# (0, 3)
# (1, 0)

a[d]
# array([0, 1, 2, 3, 4])

a[0][0]
# 0
a[1][1]
# 5
a[-1][-1]
# 15

a[0:1, 1:3]
# array([[1, 2]])
a[0:3, 2:]
# array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])

index = np.nonzero(a < 5)
type(index)

import os

os.getcwd()

os.chdir('/Users/zacks/Desktop/Code/Python/Projects')

import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/ZacksAmber/Code/master/Python/Projects/MLB.csv")
df.head()

np_baseball[:, 3]

df.isnull()

np.corrcoef(df['Height(inches)'][:100], df['Weight(pounds)'][:100])
# array([[1.        , 0.54518481],
#        [0.54518481, 1.        ]])

np_baseball = np.array(df)
np.corrcoef(np_baseball[:100, 3].astype(float), np_baseball[:100, 4].astype(float))
# array([[1.        , 0.54518481],
#        [0.54518481, 1.        ]])

df[df.iloc[:, 3]]
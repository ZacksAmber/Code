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
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in d:
    print(x)
# brand
# model
# year

for x, y in d.items():
    print(x, y)
# brand Ford
# model Mustang
# Year 1964


s = set(("apple", "banana", "cherry")) # note the double round-brackets
s
# {'apple', 'banana',

d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d.update({'brand': 'Ford', 'brand': 'Chevrolet'})
d
# {'brand': 'Chevrolet', 'model': 'Mustang', 'year': 1964}

d = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d.update({'brand': 'Ford', 'brand': 'Chevrolet', 'year': 1964, 'year': 2020})
d
# {'brand': 'Chevrolet', 'model': 'Mustang', 'year': 2020}

x = float(1)
type(x)

ccp = """ The most crazy terrorist organization,
which is no democracy, no freedom, and no human right.
It must be destroyed on 2020."""
print(ccp)
"""The most crazy terrorist organization,
which is no democracy, no freedom, and no human right.
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
    print(x, y)
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



def exp(b, n):
    if n == 0:
        return 1
    elif n > 0:
        result = b * exp(b, n)
        n - 1


exp(2, 2)

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
    "Name": "Zacks",
    "Age": 25,
    "Country": "United States"
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
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'exp']
"""

import tmp
dir(tmp)
"""
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'person']
"""

import platform
dir(platform)
"""
['_WIN32_CLIENT_RELEASES',
 '_WIN32_SERVER_RELEASES',
 '__builtins__',
 '__cached__',
 '__copyright__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 '__version__',
 '_comparable_version',
 '_component_re',
 '_default_architecture',
 '_follow_symlinks',
 '_ironpython26_sys_version_parser',
 '_ironpython_sys_version_parser',
 '_java_getprop',
 '_libc_search',
 '_mac_ver_xml',
 '_node',
 '_norm_version',
 '_platform',
 '_platform_cache',
 '_pypy_sys_version_parser',
 '_sys_version',
 '_sys_version_cache',
 '_sys_version_parser',
 '_syscmd_file',
 '_syscmd_uname',
 '_syscmd_ver',
 '_uname_cache',
 '_ver_output',
 '_ver_stages',
 'architecture',
 'collections',
 'java_ver',
 'libc_ver',
 'mac_ver',
 'machine',
 'node',
 'os',
 'platform',
 'processor',
 'python_branch',
 'python_build',
 'python_compiler',
 'python_implementation',
 'python_revision',
 'python_version',
 'python_version_tuple',
 're',
 'release',
 'sys',
 'system',
 'system_alias',
 'uname',
 'uname_result',
 'version',
 'win32_edition',
 'win32_is_iot',
 'win32_ver']
"""

import sys
sys.path
"""
['/private/CHAR/folders/31/lj6nmqhx1711vgv7r7g9r_cm0000gp/T/9c5d056e-aad5-4997-99e9-b8991b740258',
 '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
 '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
 '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
 '',
 '/Users/zack/Library/Python/3.8/lib/python/site-packages',
 '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages',
 '/Users/zack/Library/Python/3.8/lib/python/site-packages/IPython/extensions',
 '/Users/zack/.ipython']
 """

import platform
print(platform.python_version())
# 3.8.1

import sys
sys.path
"""
['/private/CHAR/folders/31/lj6nmqhx1711vgv7r7g9r_cm0000gp/T/c1b404a3-2753-4a56-931a-20c02831e04f',
 '/Users/zack/.vscode/extensions/ms-python.python-2020.1.58038/pythonFiles',
 '/Users/zack/.vscode/extensions/ms-python.python-2020.1.58038/pythonFiles/lib/python',
 '/Users/zack/opt/anaconda3/lib/python37.zip',
 '/Users/zack/opt/anaconda3/lib/python3.7',
 '/Users/zack/opt/anaconda3/lib/python3.7/lib-dynload',
 '',
 '/Users/zack/opt/anaconda3/lib/python3.7/site-packages',
 '/Users/zack/opt/anaconda3/lib/python3.7/site-packages/aeosa',
 '/Users/zack/opt/anaconda3/lib/python3.7/site-packages/IPython/extensions',
 '/Users/zack/.ipython']
"""

import sys
sys.path.append("/tmp")
sys.path
"""
['/private/CHAR/folders/31/lj6nmqhx1711vgv7r7g9r_cm0000gp/T/c1b404a3-2753-4a56-931a-20c02831e04f',
 '/Users/zack/.vscode/extensions/ms-python.python-2020.1.58038/pythonFiles',
 '/Users/zack/.vscode/extensions/ms-python.python-2020.1.58038/pythonFiles/lib/python',
 '/Users/zack/opt/anaconda3/lib/python37.zip',
 '/Users/zack/opt/anaconda3/lib/python3.7',
 '/Users/zack/opt/anaconda3/lib/python3.7/lib-dynload',
 '',
 '/Users/zack/opt/anaconda3/lib/python3.7/site-packages',
 '/Users/zack/opt/anaconda3/lib/python3.7/site-packages/aeosa',
 '/Users/zack/opt/anaconda3/lib/python3.7/site-packages/IPython/extensions',
 '/Users/zack/.ipython',
 '/tmp']
"""

import datetime
dir(datetime)
"""
['MAXYEAR',
 'MINYEAR',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'date',
 'datetime',
 'datetime_CAPI',
 'sys',
 'time',
 'timedelta',
 'timezone',
 'tzinfo']
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
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
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
    "name": "John",
    "age": 30,
    "city": "New York"
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
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
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
    ],
    "pets" = null.
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
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
}
"""

import camelcase

c = camelcase.CamelCase() # #This method capitalizes the first letter of each word.
txt = "hello world"
print(c.hump(txt))
# Hello World


import mysql.connector

root_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='00GUNDAM7Sword/GM',
    auth_plugin='mysql_native_password'
)

mysql_root = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='00GUNDAM7Sword/GM'
)

import mysql.connector

root_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password'



import mysql.connector

mysql_root = mysql.connector.connect(
    host="localhost",
    user="your_username",
    passwd="your_password"
)

root_cursor = mysql_root.cursor()

root_cursor.execute("CREATE DATABASE mydatabase")

root_cursor.execute("CREATE USER 'test'@'localhost' \
    IDENTIFIED WITH caching_sha2_password BY 'passwd' \
    PASSWORD EXPIRE INTERVAL 30 DAY \
    FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;")

import mysql.connector

mysql_test = mysql.connector.connect(
    host="localhost",
    user="test",
    passwd="passwd"
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
    host="localhost",
    user="test",
    passwd="passwd",
    database="BOS311"
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
    host="cloud-analytics-db.crmnbmzm85lc.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="Test1234",
    database="bosbot"
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
    host="localhost",
    user="test",
    passwd="passwd",
    database="BOS311"
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
    host="localhost",
    user="test",
    passwd="passwd",
    database="BOS311"
)

test_cursor = mysql_test.cursor()

sql = "SELECT * FROM test WHERE location_zipcode='02155'"

test_cursor.execute(sql)

result = test_cursor.fetchall()



def judge_duplicated():
    sql = "SELECT * FROM test WHERE reason = '{0}' AND location_zipcode = '{1}' AND '{2}'".format(
    case_information['reason'],
    case_information['location_zipcode'],
    case_information['location_street_name']
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
        case_information['reason'],
        case_information['location_zipcode'],
        case_information['location_street_name'],
        case_information['case_status'],
        case_information['open_dt']
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
        case_information['reason'],
        case_information['location_zipcode'],
        case_information['location_street_name'],
        case_information['case_status'],
        case_information['open_dt']
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
    host="cloud-analytics-db.crmnbmzm85lc.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="Test1234",
    database="bosbot"
)

SELECT priority FROM test_2020 WHERE case_status = "Open" AND reason = "Street Lights" AND location = "15 Sudbury St  Boston  MA  02203";

UPDATE test_2020 SET priority = 2 WHERE case_status = "Open" AND reason = "Street Lights" AND location = "15 Sudbury St  Boston  MA  02203"

length = 0
sql = "UPDATE {0} SET priority = {1} WHERE case_status = '{2}' AND reason = '{3}' AND location = '{4}'".format(
    mysql_table,
    length,
    case_information['reason'],
    case_information['location'],
    case_information['case_status']
)

case_information

def judge_duplicate():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
    mysql_table,
    case_information['reason'],
    case_information['location']
)
    global result

    mysql.execute(sql)
    result = mysql.fetchall()

    

    global nums_of_duplicate

    if len(result) > 0:
        nums_of_duplicate = len(result)
        return(result)
    else:
        nums_of_duplicate = None
        return(result)


def mysql_raise_priority():
    if case_information['priority'] > 5:
        case_information['priority'] = 5
    else:
        case_information['priority']+= 1

    sql = "UPDATE {0} SET priority = {1} WHERE case_status = '{2}' AND reason = '{3}' AND location = '{4}'".format(
        mysql_table,
        case_information['priority'],
        case_information['case_status'],
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)

case_information['priority'] = 0

UPDATE test_2020 SET priority = 2 WHERE case_status = "Open" AND reason = "Street Lights" AND location = "15 Sudbury St  Boston  MA  02203";

SELECT priority from test_2020 WHERE case_status = "Open" AND reason = "Street Lights" AND location = "15 Sudbury St  Boston  MA  02203";


###

import mysql.connector

# Define a function to connect MySQL
def mysql_login(mysql_host, mysql_user, mysql_passwd, mysql_database):
    global mysql_connect

    mysql_connect = mysql.connector.connect(
        host = mysql_host,
        user = mysql_user,
        passwd = mysql_passwd,
        database = mysql_database
    )

# Set login information
mysql_login(
    mysql_host = "localhost",
    mysql_user = "test",
    mysql_passwd = "passwd",
    mysql_database = "BOS311"
    )

# Set MySQL cursor
mysql = mysql_connect.cursor()

# Set MySQL table
mysql_table = "test_2020"

# Set the values
case_information = {}
case_information['priority'] = 1
case_information['case_status'] = 'Open'
case_information['reason'] = 'Street Lights'
case_information['location'] = '15 Sudbury St  Boston  MA  02203'

# Define a function raise the priority
def mysql_raise_priority():
    sql = "UPDATE {0} SET priority = {1} WHERE case_status = '{2}' AND reason = '{3}' AND location = '{4}'".format(
        mysql_table,
        case_information['priority'],
        case_information['case_status'],
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    mysql_connect.commit()
    print(mysql.rowcount, "record(s) affected")

mysql_raise_priority()



case_information['priority'] = 100
def mysql_raise_priority():
    if case_information['priority'] > 5:
        case_information['priority'] = 5
    else:
        case_information['priority']+= 1

    sql = "UPDATE {0} SET priority = {1} WHERE case_status = '{2}' AND reason = '{3}' AND location = '{4}'".format(
        mysql_table,
        case_information['priority'],
        case_information['case_status'],
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    mysql_connect.commit()
    print(mysql.rowcount, "record(s) affected")

mysql_raise_priority()


sql = "INSERT INTO " + mysql_table + " (case_enquiry_id, open_dt, target_dt, closed_dt, ontime, case_status, closure_reason, case_title, subject, reason, type, queue, department, submittedphoto, closedphoto, location, fire_district, pwd_district, city_council_district, police_district, neighborhood, neighborhood_services_district, ward, precinct, location_street_name, location_zipcode, latitude, longitude, source, email, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

val = (0, datetime.datetime.now().date().isoformat(), None, None, None, 'Open', None, case_information['case_title'], None, case_information['reason'], None, None, None, None, None, case_information['location'], None, None, None, None, None, None, None, None, None, None, None, None, case_information['source'], case_information['email'], 1)

mysql.execute(sql, val)
mysql_connect.commit()
print(mysql.rowcount, "record inserted.")


case_information

val[0][1]

l = []
for x in range(len(val)):
    l.append(val[x][1])

tuple(l)

val = [
    ('case_enquiry_id', None),
    ('open_dt', datetime.datetime.now().date().isoformat()),
    ('target_dt', None),
    ('closed_dt', None),
    ('ontime', None),
    ('case_status', 'Open'),
    ('closure_reason', None),
    ('case_title', "API"),
    ('subject', None),
    ('reason', "API"),
    ('type', None),
    ('queue', None),
    ('department', None),
    ('submittedphoto', None),
    ('closedphoto', None),
    ('location', "API"),
    ('fire_district', None),
    ('pwd_district', None),
    ('city_council_district', None),
    ('police_district', None),
    ('neighborhood', None),
    ('neighborhood_services_district', None),
    ('ward', None),
    ('precinct', None),
    ('location_street_name', None),
    ('location_zipcode', None),
    ('latitude', None),
    ('longitude', None),
    ('source', "API"),
    ('email', "API"),
    ('priority', 1)
]

mysql.execute(sql, val)

mysql_conncet.commit()

print(mysql.rowcount, "record inserted.")

sql = 'select * from {0} limit 1'.format(mysql_table)
mysql.execute(sql)

result = mysql.fectall()


def case(open_dt, case_status, case_title, reason, location, source, email, priority):
    global case_information

    case_information = {
    'case_enquiry_id': None,
    'open_dt': open_dt,
    'target_dt': None,
    'closed_dt': None,
    'ontime': None,
    'case_status': case_status,
    'closure_reason': None,
    'case_title': case_title,
    'subject': None,
    'reason': reason,
    'type': None,
    'queue': None,
    'department': None,
    'submittedphoto': None,
    'closedphoto': None,
    'location': location,
    'fire_district': None,
    'pwd_district': None,
    'city_council_district': None,
    'police_district': None,
    'neighborhood': None,
    'neighborhood_services_district': None,
    'ward': None,
    'precinct': None,
    'location_street_name': None,
    'location_zipcode': None,
    'latitude': None,
    'longitude': None,
    'source': source,
    'email': email,
    'priority:': priority
    }

    return(case_information)


sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
    mysql_table,
    case_information['reason'],
    case_information['location']
)

mysql.execute(sql)
result = mysql.fetchall()

result
result = []

try:
    case_information
except NameError:
    pass
else:
    case_information.clear()

l = []
for i in result:
    l.append(i[5]) # extract case_status


l = []
for i in result:
    l.append(i[1][0:10]) # extract date

if '2020-01-31' in l:
    print(1)

del(result)


sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}' AND open_dt LIKE '{3}%'".format(
    mysql_table,
    case_information['reason'],
    case_information['location'],
    case_information['open_dt']
)

mysql.execute(sql)
result = mysql.fetchall()

result
del(result)

l = []
for i in result:
    l.append(i[1][0:10]) # extract date

if '2020-01-31' in l: # extract the date part from open_dt. e.g, '2020-01-31 14:35:46' > '2020-01-31'
    return(result)
else:
    return(None)

"15 Sudbury St  Boston  MA  02203"
"15 Sudbury St  Boston  MA  02203" is "15 Sudbury St  Boston  MA  02203"

"15 Sudbury St  Boston  MA  02203".replace(" ","")


boston in 



"13 stree" in "13       street"
"13       street" in "13 stree"



case(
    open_dt = datetime.datetime.now().date().isoformat(),
    case_status = "Open",
    case_title = "Situation 1",
    reason = "Street Lights",
    location = "000 Huntington Ave  Boston  MA  02203",
    source = "ChatBot",
    email = "test@gmail.com",
    priority = 1
)

case(
    open_dt = datetime.datetime.now().date().isoformat(),
    case_status = "Open",
    case_title = "Situation 2",
    reason = "Enforcement & Abandoned Vehicles",
    location = "15 Sudbury St  Boston  MA  02203",
    source = "ChatBot",
    email = "test@gmail.com",
    priority = 1
)

case(
    open_dt = "2020-01-31", # Assume today is 2020-01-31,
    case_status = "Open",
    case_title = "Situation 3",
    reason = "Enforcement & Abandoned Vehicles",
    location = "15 Sudbury St  Boston  MA  02203",
    source = "ChatBot",
    email = "test@gmail.com",
    priority = 1
)

case(
    open_dt = datetime.datetime.now().date().isoformat(),
    case_status = "Open",
    case_title = "Situation 4",
    reason = "Street Lights",
    location = "15 Sudbury St  Boston  MA  02203",
    source = "ChatBot",
    email = "test@gmail.com",
    priority = 1
)


delete from test_2020 where case_enquiry_id = 0;




sql = input("Input your SELECT sentence: ")

mysql.execute(sql)
result = mysql.fetchall()

if mysql.rowcount == 0:
    print("Empty set")
elif mysql.rowcount == 1:
    print("1 row in set")
else:
    print("{0} rows in set".format(mysql.rowcount))


result[0][14] == ""

for col in result:
    for val in col:
        if val == "":
            print("None" + ",")
        else:
            print("'{0}',".format(val))

for col in result:
    for val in col:
        print(val)

101003158348
val1 = (
    '',
    '2020-01-13 12:40:13',
    '2020-01-14 12:40:12',
    '2020-01-13 13:09:24',
    'ONTIME',
    'Closed',
    'Case Closed. Closed date : 2020-01-13 13:09:24.703 Case Noted hydrant clear',
    'Parking Enforcement',
    'Transportation - Traffic Division',
    'Enforcement & Abandoned Vehicles',
    'Parking Enforcement',
    'BTDT_Parking Enforcement',
    'BTDT',
    'https://311.boston.gov/media/boston/report/photos/5e1cab6d7505d0628e5f3794/report.jpg',
    None,
    '15 Sudbury St  Boston  MA  02203',
    '3',
    '1B',
    '2',
    'A1',
    'Boston',
    '3',
    '3',
    '306',
    '15 Sudbury St',
    '2203',
    '42.3614',
    '-71.0601',
    'Citizens Connect App',
    None,
    '1'
)

101003176201
val2 = (
    '',
    '2020-01-22 21:32:00',
    '2020-02-06 08:30:00',
    None,
    'ONTIME',
    'Open',
    ' ',
    'PRINTED: EricHuynh / Street Light Outages ',
    'Public Works Department',
    'Street Lights',
    'Street Light Outages',
    'PWDx_Street Light Outages',
    'PWDx',
    None,
    None,
    '15 Sudbury St  Boston  MA  02203',
    '3',
    '1B',
    '2',
    'A1',
    'Boston',
    '3',
    '3',
    '306',
    '15 Sudbury St',
    '2203',
    '42.3614',
    '-71.0601',
    'Citizens Connect App',
    None,
    '1'
)

101003184198
val3 = (
    '',
    '2020-01-31 14:35:46',
    '2020-02-03 14:35:46',
    '2020-01-31 14:55:00',
    'ONTIME',
    'Closed',
    'Case Closed. Closed date : 2020-01-31 14:55:00.36 Case Resolved area enforced',
    'Parking Enforcement',
    'Transportation - Traffic Division',
    'Enforcement & Abandoned Vehicles',
    'Parking Enforcement',
    'BTDT_Parking Enforcement',
    'BTDT',
    'https://311.boston.gov/media/boston/report/photos/5e3481897505dbb1e2eb753a/report.jpg',
    None,
    '15 Sudbury St  Boston  MA  02203',
    '3',
    '1B',
    '2',
    'A1',
    'Boston',
    '3',
    '3',
    '306',
    '15 Sudbury St',
    '2203',
    '42.3614',
    '-71.0601',
    'Citizens Connect App',
    None,
    '1'
)

mysql_table = "sample_311"

sql = "INSERT INTO " + mysql_table + " (case_enquiry_id, open_dt, target_dt, closed_dt, ontime, case_status, closure_reason, case_title, subject, reason, type, queue, department, submittedphoto, closedphoto, location, fire_district, pwd_district, city_council_district, police_district, neighborhood, neighborhood_services_district, ward, precinct, location_street_name, location_zipcode, latitude, longitude, source, email, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

val = (0, case_information['open_dt'], None, None, None, 'Open', None, case_information['case_title'], None, case_information['reason'], None, None, None, None, None, case_information['location'], None, None, None, None, None, None, None, None, None, None, None, None, case_information['source'], case_information['email'], 1)

mysql.execute(sql, val1)
mysql_connect.commit()
print(mysql.rowcount, "record inserted.")

mysql.execute(sql, val2)
mysql_connect.commit()
print(mysql.rowcount, "record inserted.")

mysql.execute(sql, val3)
mysql_connect.commit()
print(mysql.rowcount, "record inserted.")



def situation_1():
    case(
        open_dt = datetime.datetime.now().date().isoformat(),
        case_status = "Open",
        case_title = "Situation 1",
        reason = "Illegal Parking",
        location = "360 Huntington Ave  Boston  MA  02115",
        source = "ChatBot",
        email = "test_1@gmail.com",
        priority = 1
    )
    return(case_information)

SELECT * FROM sample_311 WHERE reason = "Illegal Parking" AND location = "360 Huntington Ave  Boston  MA  02115" \G

def situation_2():
    case(
        open_dt = datetime.datetime.now().date().isoformat(),
        case_status = "Open",
        case_title = "Situation 2",
        reason = "Enforcement & Abandoned Vehicles",
        location = "15 Sudbury St  Boston  MA  02203",
        source = "ChatBot",
        email = "test_2@gmail.com",
        priority = 1
    )
    return(case_information)

SELECT * FROM sample_311 WHERE reason = "Enforcement & Abandoned Vehicles" AND location = "15 Sudbury St  Boston  MA  02203" \G

def situation_3():
    case(
        open_dt = "2020-01-31", # Assume today is 2020-01-31,
        case_status = "Open",
        case_title = "Situation 3",
        reason = "Enforcement & Abandoned Vehicles",
        location = "15 Sudbury St  Boston  MA  02203",
        source = "ChatBot",
        email = "test_3@gmail.com",
        priority = 1
    )
    return(case_information)

SELECT * FROM sample_311 WHERE reason = "Enforcement & Abandoned Vehicles" AND location = "15 Sudbury St  Boston  MA  02203" \G

def situation_4():
    case(
        open_dt = datetime.datetime.now().date().isoformat(),
        case_status = "Open",
        case_title = "Situation 4",
        reason = "Illegal Parking",
        location = "360 Huntington Ave  Boston  MA  02115",
        source = "ChatBot",
        email = "test_4@gmail.com",
        priority = 1
    )
    return(case_information)

SELECT * FROM sample_311 WHERE reason = "Illegal Parking" AND location = "360 Huntington Ave  Boston  MA  02115" \G

import datetime
def time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

time()

datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")[0:10]

if datetime.datetime.now().date().isoformat() in l:
    return(result)
else:
    return(None)



d ={'sssss':'ddddd'}
d['sssss'][0:3]


sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}' AND open_dt LIKE '%{3}%'".format(
    mysql_table,
    case_information['reason'],
    case_information['location'],
    case_information['open_dt'][0:10]
)

sql = "SELECT * FROM sample_311 WHERE open_dt like '%2020-01-13%'"

mysql.execute(sql)
result = mysql.fetchall()

result[0][1]

l = []
for i in result:
    l.append(i[1]) # extract date

import re

txt = "Stand with Hongkong. Overthrow CCP"

#x = re.search("^H.*P$", txt) # Starts with H

x = re.search("^S.*P$", txt) # Starts with H

if (x):
  print("YES! We have a match!")
else:
  print("No match")


import datetime

def time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

time()

Kobe_Bryant = datetime.datetime(2020, 1, 26, 15, 50, 23)
print(Kobe_Bryant.strftime("%Y-%m-%d %H:%M:%S"))

import re

re.findall("[a-m]", "Amber") # Returns a list containing all matches
# ['m', 'b', 'e']

re.findall("[a-m]", "amber") # Returns a list containing all matches with case sensitive
# ['a', 'm', 'b', 'e']

re.findall("[a-m]", "Amber m") # Returns a list containing all matches in the original sequence
# ['m', 'b', 'e', 'm']



re.search("\a", "Amber")
# <re.Match object; span=(1, 2), match='m'>
re.search("[a-m]", "Amber").start()

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

import re

China = "The Chinese Communist Party will disintegrate in 2020."

re.findall("[a-e]", China) # Returns a list containing all matches in the original sequence and case sentitive.
# ['e', 'e', 'e', 'a', 'd', 'e', 'a', 'e']

re.findall("\d", China) # Find all digit characters:
# ['2', '0', '2', '0']

re.findall("Pa..y", China) # Search for a sequence that starts with "Pa", followed by two (any) characters, and an "y":
# ['Party']

re.findall("^The", China) # Check if the string starts with 'The':
# ['The']

re.findall("2020[.]$", China) # Check if the string ends with '2020.':
# ['2020.']

re.findall("isx*", China) # Check if the string contains "is" followed by 0 or more "x" characters. It returns 'is' twice because 'x' occures 0 time.
# ['is', 'is']

re.findall("ine+", China) # Check if the string contains "in" followed by 1 or more "e" characters:
# ['ine']

re.findall("om{2}", China) # Check if the string contains "o" followed by exactly two "m" characters:
# ['omm']

re.findall("Chi|Com", China) # Check if the string contains either "Chi" or "Com":
# ['Chi', 'Com']

re.findall("(Par)", China) # Put a series characters in a group. In this case, it is the same as "Par".

re.findall("(ine)(se)*", China) # Check if the string contains "ine" followed by 0 or more "se" characters:
# [('ine', 'se')]

re.findall("inese*", China)  # Check if the string contains "ines" followed by 0 or more "e" characters:
# ['inese']

re.findall("(ine)(xx)*", China) # Check if the string contains "ine" followed by 0 or more "xx" characters:
# [('ine', '')]


re.search("C", China) # Returns a Match object if there is a match anywhere in the string
# <re.Match object; span=(4, 5), match='C'>

re.findall("\AThe", China) # Returns a match if the specified characters are at the beginning of the string
# ['The']

re.search("Chin", China) # 
# <re.Match object; span=(4, 8), match='Chin'>

re.split("\s", China) # Returns a list where the string has been split at each match + Returns a match where the string contains a white space character
# ['The', 'Chinese', 'Communist', 'Party', 'will', 'disintegrate', 'in', '2020.']


import re

China = "The Chinese Communist Party will disintegrate in 2020."

re.findall("\AThe", China) # Check if the string starts with "The":
# ['The']
re.findall("\AThe", China) == re.findall("^The", China)
# True

# Note: Prefix r or R is used for escaping sequence.
print('a\\ab') # Backslash (\)
# a\ab
print('aa\ab') # ASCII Bell (BEL)
# aab
print('aa\bb') # ASCII Backspace (BS)
# ab
print('aa\fb') # Formfeed
# aa
#   b
print('aa\nb') # ASCII Linefeed (LF)
# aa
# b
print('aa\rb') # Carriage Return
# b
print('aa\tb') # ASCII Horizontal Tab (TAB
# aa	b
print('aa\vb') # ASCII Vertical Tab (VT)
# aa
#   b

re.findall(r"\bThe", China) # Check if the string starts or ends with "The":
# ['The']
re.findall(r"\b2020[.]", China) # Check if the string starts or ends with "2020.":
# ['2020.']

re.findall(r'\BChi', China) # Check if "Chi" is present, but NOT at the beginning of a word:
# []
re.findall(r'\Bhi', China) # Check if "hi" is present, but NOT at the beginning of or at the end of a WORD:
# hi

re.findall('\d', China) # Check if the string contains any digits (numbers from 0-9):
# ['2', '0', '2', '0']

re.findall('\D', China) # Return a match at every no-digit character:
"""
['T',
 'h',
 'e',
 ' ',
 'C',
 'h',
 'i',
 'n',
 'e',
 's',
 'e',
 ' ',
 'C',
 'o',
 'm',
 'm',
 'u',
 'n',
 'i',
 's',
 't',
 ' ',
 'P',
 'a',
 'r',
 't',
 'y',
 ' ',
 'w',
 'i',
 'l',
 'l',
 ' ',
 'd',
 'i',
 's',
 'i',
 'n',
 't',
 'e',
 'g',
 'r',
 'a',
 't',
 'e',
 ' ',
 'i',
 'n',
 ' ',
 '.']
"""

re.findall('\s', China) # Return a match at every white-space character:
# [' ', ' ', ' ', ' ', ' ', ' ', ' ']
re.search('\s', China)
# <re.Match object; span=(3, 4), match=' '>
re.split('\s', China)
# ['The', 'Chinese', 'Communist', 'Party', 'will', 'disintegrate', 'in', '2020.']

re.findall('\S', China) # Return a match at every NON white-space character:
"""
['T',
 'h',
 'e',
 'C',
 'h',
 'i',
 'n',
 'e',
 's',
 'e',
 'C',
 'o',
 'm',
 'm',
 'u',
 'n',
 'i',
 's',
 't',
 'P',
 'a',
 'r',
 't',
 'y',
 'w',
 'i',
 'l',
 'l',
 'd',
 'i',
 's',
 'i',
 'n',
 't',
 'e',
 'g',
 'r',
 'a',
 't',
 'e',
 'i',
 'n',
 '2',
 '0',
 '2',
 '0',
 '.']
"""

re.findall('\w', China) # Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
"""
['T',
 'h',
 'e',
 'C',
 'h',
 'i',
 'n',
 'e',
 's',
 'e',
 'C',
 'o',
 'm',
 'm',
 'u',
 'n',
 'i',
 's',
 't',
 'P',
 'a',
 'r',
 't',
 'y',
 'w',
 'i',
 'l',
 'l',
 'd',
 'i',
 's',
 'i',
 'n',
 't',
 'e',
 'g',
 'r',
 'a',
 't',
 'e',
 'i',
 'n',
 '2',
 '0',
 '2',
 '0']
"""

re.findall('\W', China) # Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', '.']

re.findall('2020[.]\Z', China) # Check if the string ends with "2020.":
# ['2020.']
re.findall('2020[.]\Z', China) == re.findall('2020[.]$', China)
# True


import re

China = "The Chinese Communist Party will disintegrate in 2020."

re.findall('[arn]', China) # Check if the string has any a, r, or n characters:
# ['n', 'n', 'a', 'r', 'n', 'r', 'a', 'n']

re.findall('[a-n]', China) # Check if the string has any characters between a and n:
"""
['h',
 'e',
 'h',
 'i',
 'n',
 'e',
 'e',
 'm',
 'm',
 'n',
 'i',
 'a',
 'i',
 'l',
 'l',
 'd',
 'i',
 'i',
 'n',
 'e',
 'g',
 'a',
 'e',
 'i',
 'n']
"""

re.findall('[^arn]', China) # Check if the string has other characters than a, r, or n:
"""
['T',
 'h',
 'e',
 ' ',
 'C',
 'h',
 'i',
 'e',
 's',
 'e',
 ' ',
 'C',
 'o',
 'm',
 'm',
 'u',
 'i',
 's',
 't',
 ' ',
 'P',
 't',
 'y',
 ' ',
 'w',
 'i',
 'l',
 'l',
 ' ',
 'd',
 'i',
 's',
 'i',
 't',
 'e',
 'g',
 't',
 'e',
 ' ',
 'i',
 ' ',
 '2',
 '0',
 '2',
 '0',
 '.']
"""

re.findall('[0123]', China) # Check if the string has any 0, 1, 2, or 3 digits:
# ['2', '0', '2', '0']

re.findall('[0-9]', China) # Check if the string has any digits:
# ['2', '0', '2', '0']
re.findall('[0-9]', China) == re.findall('\d', China)
# True

re.findall('[0-5][0-9]', China) # Check if the string has any two-digit numbers, from 00 to 59:
# ['20', '20']

re.findall('[a-zA-Z]', China) # Check if the string has any characters from a to z lower case, and A to Z upper case:
"""
['T',
 'h',
 'e',
 'C',
 'h',
 'i',
 'n',
 'e',
 's',
 'e',
 'C',
 'o',
 'm',
 'm',
 'u',
 'n',
 'i',
 's',
 't',
 'P',
 'a',
 'r',
 't',
 'y',
 'w',
 'i',
 'l',
 'l',
 'd',
 'i',
 's',
 'i',
 'n',
 't',
 'e',
 'g',
 'r',
 'a',
 't',
 'e',
 'i',
 'n']
"""
re.findall('[a-zA-Z0-9_]', China) == re.findall('\w', China)
# True

re.findall('[.]', China) # Check if the string has any . characters:
# ['.']


import re

China = "The Chinese Communist Party will disintegrate in 2020."

re.findall('^The.*2020[.]$', China) # Check if the string starts with "The" and ends with "2020.":
# 'The Chinese Communist Party will disintegrate in 2020.']


import re

China = "The Chinese Communist Party will disintegrate in 2020."

re.findall('\s', China) # Return a match at every white-space character:
# [' ', ' ', ' ', ' ', ' ', ' ', ' ']
re.search('\s', China)
# <re.Match object; span=(3, 4), match=' '>
re.search('\s', China).start()
# 3
re.split('\s', China)
# ['The', 'Chinese', 'Communist', 'Party', 'will', 'disintegrate', 'in', '2020.']

import re

China = "The Chinese Communist Party will disintegrate in 2020."

print(re.search('[!]', China))
# None

re.split('\s', China, 1)
# ['The', 'Chinese Communist Party will disintegrate in 2020.']


import re

China = "The Chinese Communist Party will disintegrate in 2020."

re.sub('\s', 'X', China, 2) # Replace all white-space characters with the character 'X'
# 'TheXChineseXCommunist Party will disintegrate in 2020.'


import re

China = "The Chinese Communist Party will disintegrate in 2020."

re.search(r'\bP\w+', China) # Search for an upper case "P" character in the beginning of a word, and print its position:
# <re.Match object; span=(22, 27), match='Party'>

re.search(r'\bP\w+', China).span()
# (22, 27)


import re

China = "The Chinese Communist Party will disintegrate in 2020."

re.search(r'\bP\w+', China)
# <re.Match object; span=(22, 27), match='Party'>

re.search(r'\bP\w+', China).group() # Search for an upper case "P" character in the beginning of a word, and print the word:
# 'Party'

re.search(r'\bW\w+', China).group() # Search for an upper case "W" character in the beginning of a word, and print the word:
# AttributeError: 'NoneType' object has no attribute 'group'


print(x)
# NameError: name 'x' is not defined

try:
  print(x)
except:
  print("An exception occurred")
# An exception occurred

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
# Variable x is not defined

#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
# Hello
# Nothing went wrong

try:
    print(x)
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
  print("The 'try except' is finished")
# Something went wrong
# The 'try except' is finished

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
  print("The 'try except' is finished")
# Hello
# Nothing went wrong
# The 'try except' is finished

import os

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
# Something went wrong when writing to the file
# NameError: name 'f' is not defined. We do not have a file named "demofile.txt", so we cannot open it. And f is never be daclared. The finally block will raise a error.

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    if f in globals():
        f.close()

globals()
locals()

x in globals()

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")
# Exception: Sorry, no numbers below zero

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
# TypeError: Only integers are allowed

username = input("Enter username:")
print("Username is: " + username)
# Username is: Zacks


age = 25

print("I am " + age + " year's old")
# TypeError: can only concatenate str (not "int") to str

print("I am {} year's old".format(age))
# I am 25 year's old

name = "Zacks"
age = 25
country = "United States"

Introduction = "I am {name}. {name} is {age:.2f} year's old, and live in {country}."
print(Introduction.format(age, name, country))
# KeyError: 'name'

import os
os.getcwd()
os.chdir("/Users/zacks/Desktop/Code/Python")

f = open("demofile.txt", "r")
f.read(5) # Return the 5 first characters of the file:
# 'Hello'

f = open("demofile.txt", "r")
print(f.readline()) # Read one line of the file:
# Hello! Welcome to demofile.txt
print(f.readline())
# This file is for testing purposes.

f = open("demofile.txt", "r")
for lines in f:
    print(lines)
# Hello! Welcome to demofile.txt

# This file is for testing purposes.

# Good Luck!

f = open("demofile.txt", "r")
print(f.readline())
# Hello! Welcome to demofile.txt
f.close()

with open("demofile.txt", "r") as f:
    print(f.read())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

with open("demofile.txt", "a") as f: # Open the file "demofile.txt" and append content to the file:
    f.write("Now the file has more content!")

with open("demofile.txt", "r") as f: # Open the file "demofile.txt" and read the content:
    print(f.read())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!
# Now the file has more content!


with open("demofile.txt", "w") as f: # Open the file "demofile.txt" and overwrite content to the file:
    f.write("Woops! I have deleted the content!")

with open("demofile.txt", "r") as f: # Open the file "demofile.txt" and read the content:
    print(f.read())
# Woops! I have deleted the content!

f = open("myfile.txt", "a")

f = open("myfile2.txt", "w")

import os
os.remove("demofile.txt")

import os

os.path.exists("myfile.txt")
# True

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

sum = 0

for i in speed:
    sum = sum + i

mean = sum/len(speed)

print(mean)
# 89.76923076923077

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = numpy.mean(speed)

print(mean)
# 89.76923076923077

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

speed.sort()

x = len(speed)/2

if x % 2 == 0.0:
    print((speed[int(x-1)] + speed[int(x)])/2)
else:
    print(speed[int(x)])
# 87

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

median = numpy.median(speed)

print(median)
# 87.0

speed = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]

median = numpy.median(speed)

print(median)
# 86.5

speed = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]

speed.sort()

x = len(speed)/2

if x % 2 == 0.0:
    print((speed[int(x-1)] + speed[int(x)])/2)
else:
    print(speed[int(x)])

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mode = stats.mode(speed)

print(mode)
# ModeResult(mode=array([86]), count=array([3]))

print(mode[0][0])
# 86

import numpy

speed = [86,87,88,86,87,85,86]
Variance = numpy.var(speed)
print(Variance)
# 

import numpy

speed = [86,87,88,86,87,85,86]
SD = numpy.std(speed)


import numpy

# Standard Deviation - Population
speed = [86,87,88,86,87,85,86]
numpy.std(speed)
# 0.9035079029052513

# Standard Deviation - Sample
speed = [86,87,88,86,87,85,86]
numpy.std(speed, ddof = 1) # ddof: Degree of freedom
# 0.9759000729485332



import numpy

# Variance - Population
speed = [86,87,88,86,87,85,86]
numpy.var(speed)
# 0.8163265306122449

# Variance - Sample
speed = [86,87,88,86,87,85,86]
numpy.var(speed, ddof = 1) # ddof: Degree of freedom
# 0.9523809523809524


import numpy

# Variance - Population
speed = [32,111,138,28,59,77,97]
numpy.var(speed)
# 1432.2448979591834

# Variance - Sample
speed = [32,111,138,28,59,77,97]
numpy.var(speed, ddof = 1) # ddof: Degree of freedom
# 1670.9523809523807


import numpy

# Standard Deviation - Population
speed = [32,111,138,28,59,77,97]
numpy.std(speed)
# 37.84501153334721

# Standard Deviation - Sample
speed = [32,111,138,28,59,77,97]
numpy.std(speed, ddof = 1) # ddof: Degree of freedom
# 40.877284412646354


import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

#  Percentiles
k = numpy.percentile(ages, 70)
print(k)
# 41.0

# Quartiles
numpy.percentile(ages, 25) # Q1
# 11.0

numpy.percentile(ages, 50) # Q2
# 31.0

numpy.percentile(ages, 75) # Q3
# 43.0

import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
x = np.random.normal(200, 25, size = 10000) # mu = 200, sigma = 25

plt.hist(x, bins = 'auto', normed = True， cumulative = True)
plt.title("Normal Distribution")
plt.xlabel("Range")
plt.ylabel("Relative Frequency")
plt.show()




import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)
x = np.random.normal(200, 25, size = 10000) # mu = 200, sigma = 25

fig, ax = plt.subplots(figsize=(8, 4))

# plot the cumulative histogram
n, bins, patches = ax.hist(x, n_bins, density=True, histtype='step',
                           cumulative=True, label='Empirical')

# Add a line showing the expected distribution.
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
y = y.cumsum()
y /= y[-1]

ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')

# Overlay a reversed cumulative histogram.
ax.hist(x, bins=bins, density=True, histtype='step', cumulative=-1,
        label='Reversed emp.')

# tidy up the figure
ax.grid(True)
ax.legend(loc='right')
ax.set_title('Cumulative step histograms')
ax.set_xlabel('Annual rainfall (mm)')
ax.set_ylabel('Likelihood of occurrence')

plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])


from plotnine import ggplot, geom_point, aes, stat_smooth, facet_wrap
from plotnine.data import mtcars

(ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)'))
 + geom_point()
 + stat_smooth(method='lm')
 + facet_wrap('~gear'))


import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import mtcars

# Define data as dictionary
d = {'x_value': [0, 1], 'y_value': [0, 1]}

# Convert dict to data frame
two_points = pd.DataFrame(data = d)

# Draw two points
(ggplot(two_points, # Data: tell ggplot the data source.
        aes(x = 'x_value', y = 'y_value')) + # Aesthetics: Define x
    geom_point()) # Geometric Objects: Tell ggplot what kind of plot you need.

# Connect two points
(ggplot(two_points, # Data: tell ggplot the data source.
       aes(x = 'x_value', y = 'y_value')) + # Aesthetics: Define x variables and y variables.
    geom_point() + geom_line()) # Geometric Objects: This time we connect the two points.

qplot(x = 'x_value', y = 'y_value', data = two_points, 
    geom = ['point', 'line'])

import matplotlib
import pandas as pd
import numpy as np
from plotnine import *
from plotnine.data import mtcars
%matplotlib inline

df = mtcars[["name", "mpg", "cyl", "wt"]]
df.head(6) # show the first 6 rows of data

#               name   mpg  cyl     wt
#          Mazda RX4  21.0    6  2.620
#      Mazda RX4 Wag  21.0    6  2.875
#         Datsun 710  22.8    4  2.320
#     Hornet 4 Drive  21.4    6  3.215
#  Hornet Sportabout  18.7    8  3.440
#            Valiant  18.1    6  3.460

# Basic scatter plot
qplot(x = 'mpg', y = 'wt', data = df, geom = "point")

# Scatter plot with smoothed line
qplot('mpg', 'wt', data = df, 
      geom = ["point", "smooth"])

# Scatter plot with smoothed line
(ggplot(df, aes(x = 'mpg', y = 'wt')) + 
    geom_point() +
    geom_smooth() +
    stat_smooth(method='lm'))

qplot('mpg', 'wt', data = df, color = 'cyl', shape = 'cyl')

set.seed(1234)
wdata = data.frame(
        sex = factor(rep(c("F", "M"), each=200)),
        weight = c(rnorm(200, 55), rnorm(200, 58)))
head(wdata)

import pandas as pd
import numpy as np
from plotnine import *

# Define Wight
np.random.seed(1234)
weight1 = np.random.normal(55, size = 200)
weight2 = np.random.normal(58, size = 200)
weight = np.append(weight1, weight2)

# Define sex
sex = ['F'] * 200 + ['M'] * 200

# Define Data Frame
wdata = pd.DataFrame(list(zip(sex, weight)), columns = ["Sex", "Weight"]) # zip() for zipping two lists

wdata.head(6)

"""
  Sex     Weight
0   F  55.471435
1   F  53.809024
2   F  56.432707
3   F  54.687348
4   F  54.279411
5   F  55.887163
"""

# Basic box plot from data frame
qplot('sex', 'weight', data = wdata, 
      geom = "boxplot", fill = 'sex')

# Violin plot
qplot('sex', 'weight', data = wdata, geom = "violin")

# Dot plot
qplot('sex', 'weight', data = wdata, geom = "dotplot",
      stackdir = "center", binaxis = "y", dotsize = 0.5)

# Dot plot
qplot('sex', 'weight', data = wdata, geom = "dotplot",
      stackdir = "center", binaxis = 'y', dotsize = 0.05)


# Histogram  plot
# Change histogram fill color by group (sex)
qplot('weight', data = wdata, geom = "histogram",
      fill = 'sex')

# Density plot
# Change density plot line color by group (sex)
# change line type
qplot('weight', data = wdata, geom = "density",
    color = 'sex', linetype = 'sex')
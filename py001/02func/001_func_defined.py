#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

#==========================1. 函数定义使用def关键字=================================
# 包含函数名，括号，参数，和冒号，冒号后缩进后包含函数体，函数返回值用return返回
def c_abs(x):
    if not isinstance(x, (int, float)): # 参数类型检查
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

print(f"自定义函数调用，c_abs(-99): {c_abs(-99)}")

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 函数多返回值，实际上返回的是一个tuple，语法上可以用多个变量来接收，省略tuple的括号
print(f"自定义函数调用，move(100, 100, 60, math.pi / 6) => {move(100, 100, 60, math.pi / 6)}")

#=====2. 函数的参数可以使用默认值，当不传递参数的时候，该参数为默认值, 默认参数必须只当不变对象=======
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(f"含默认参数的函数的调用，power(x, n=2)，不传递该参数使用默认值，power(2) => {power(2)}")

#==========3. 可变参数，仅仅在参数前加上*号，函数内部接受到的是一个tuple=========================
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 当通过list或者tuple传递到可变参数的函数中时，可以简略写成cals(*mylist)
print(f"可变参数函数的调用，calc(*numbers), 可以传任意多个numbers, calc(1, 2, 3) => {calc(1, 2, 3)}")

#==========4. 关键字参数，常常用来扩展函数的传参，函数内部接受到的是一个dict=======================
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 当通过dict传递到该函数的关键字参数中时，可以简略写成person('Jack', 24, **extra), 其中extra是一个dict
print(f"关键字参数函数的调用，person(name, age, **kw), 除了必传，额外可以传递任意参数，person('Bob', 35, city='Beijing') => 得到kw为city,Beijing的dict")



#===========5. 命名关键字参数，常常用来扩展函数参数，且能够限制调用者传参的方式===========================
# dict只接受city和job，两个key。与关键字参数不同，命名的关键字和必传参数间要加一个*隔开
def person2(name, age, *, city, job):
    print(name, age, city, job)



#===========总结: Python中参数这么多，总的来说，定义的顺序为必选参数、默认参数、可变参数、命名关键字参数和关键字参数


#=======================6. Python递归函数=====================================
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, functools

#===================1. Python函数装饰器=============================
# 函数对象有一个__name__属性（注意：是前后各两个下划线），可以拿到函数的名字
def now():
    print('2024-6-1')

f = now
# 函数now赋值给f，f.__name__的值为：now
print(f"函数now赋值给f，f.__name__的值为：{f.__name__}")

# 装饰器可以理解为就是一个函数的代理，在这个代理中可以扩展被代理函数的功能
# log是一个decorator，接受一个函数作为参数，并返回一个函数，借助Python的@语法，把decorator置于函数的定义处，就扩展了函数
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 把@log放到now_carry_log()函数的定义处，相当于执行了语句, now = log(now)
@log
def now_carry_log():
    print('2024-6-1')

# call now_carry_log():
# 2024-6-1
# now_carry_log函数，绑定了一个装饰器log，now_carry_log()调用时 => None
print(f"now_carry_log函数，绑定了一个装饰器log，now_carry_log()调用时 => {now_carry_log()}")

# 设计一个装饰器decorator, 可以作用任何函数上，并打印该函数的执行时间
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn

# 测试
#fast executed in 10.24 ms
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;
#slow executed in 10.24 ms
@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


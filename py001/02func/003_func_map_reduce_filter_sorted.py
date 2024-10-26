#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce

#========================1. 认识Map: 函数作用序列==============================
def f(x):
    return x * x

# 返回的r是一个Iterator, Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
# map是一个高阶函数
r = map(f, [1, 2, 3, 4, 5])

#这是Map-Reduce的Map作用后的结果list(r) => [1, 4, 9, 16, 25]
print(f"这是Map-Reduce的Map作用后的结果list(r) => {list(r)}")

#=========================2. 认识Reduce：堆积==========================
def add(x, y):
    return x + y

x = reduce(add, [1, 3, 5, 7, 9])
#这是Map-Reduce的Reduce作用后的结果x => 25
print(f"这是Map-Reduce的Reduce作用后的结果x => {x}")

#map用于将一个函数作用于一个序列，以此得到另一个序列
#reduce用于将一个函数依次作用于上次计算的结果和序列的下一个元素，以此得到最终结果。

#=========================3. 认识filter：过滤==========================
#与map有些类似，不同的是，filter()把传入的函数，以此应用每个元素，根据Bool值，过滤出最终的元素
def is_odd(n):
    return n % 2 == 1

# filter返回的也是一个Iterator
ft = filter(is_odd, [1, 2, 3, 4, 5, 6, 7])

# 这是Filter作用后过滤奇数的结果list(ft) => [1, 3, 5, 7]
print(f"这是Filter作用后过滤奇数的结果list(ft) => {list(ft)}")


#=========================4. 认识sorted排序函数========================
# 这是sorted作用后的排序结果，sorted([36, 5, -12, 9, -21]) => [-21, -12, 5, 9, 36]
print(f"这是sorted作用后的排序结果，sorted([36, 5, -12, 9, -21]) => {sorted([36, 5, -12, 9, -21])}")

# 这是sorted指定排序函数key后排序的结果， sorted([36, 5, -12, 9, -21], key=abs) => [5, 9, -12, -21, 36]
print(f"这是sorted指定排序函数key后排序的结果， sorted([36, 5, -12, 9, -21], key=abs) => {sorted([36, 5, -12, 9, -21], key=abs)}")

#这是sorted指定排序函数key后且指定降序排序的结果， sorted([36, 5, -12, 9, -21], key=abs, reverse=True) => [36, -21, -12, 9, 5]
print(f"这是sorted指定排序函数key后且指定降序排序的结果， sorted([36, 5, -12, 9, -21], key=abs, reverse=True) => {sorted([36, 5, -12, 9, -21], key=abs, reverse=True)}")



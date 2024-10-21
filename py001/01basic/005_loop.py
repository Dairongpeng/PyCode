#!/usr/bin/env python
# -*- coding: utf-8 -*-

#===================for-i循环==============================
fori_list = ['a', 'b', 'c', 'd']

for index, value in enumerate(fori_list):
    print(f"ForI: Index => {index}, Value => {value}")

#==================for-in循环，也称为迭代器==============================
forin_list = ['a', 'b', 'c', 'd']
for element in forin_list:
    print(f"ForIn: Value => {element}")

#=================while循环，也称为条件循环=============================
# 100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(f"While: Sum => {sum}")

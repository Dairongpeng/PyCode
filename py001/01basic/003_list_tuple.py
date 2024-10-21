#!/usr/bin/env python
# -*- coding: utf-8 -*-

#===================================List========================================
# python中可变有序表
classmatesList = ['Michael', 'Bob', 'Tracy']

# 向后追加一个元素, ['Michael', 'Bob', 'Tracy', 'Adam']
classmatesList.append('Adam')

# 插入元素到指定位置, ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
classmatesList.insert(1, 'Jack')

# 删除末尾元素, ['Michael', 'Jack', 'Bob', 'Tracy']
classmatesList.pop()

# 删除指定位置的元素, ['Michael', 'Bob', 'Tracy']
classmatesList.pop(1)

# 替换指定位置的元素, ['Michael', 'Sarah', 'Tracy']
classmatesList[1] = 'Sarah'

# 允许list内元素类型各不相同
L = ['python', 'java', ['asp', 'php'], 'scheme', 123, True]

#==================================Tuple=====================================
# python中的元组，和list的区别是tuple一旦初始化就不能改变了,不可变是指每个元素的指向不变。 初始化后只能获取元素，append,insert都不再支持
classmatesTuple = ('Michael', 'Bob', 'Tracy')

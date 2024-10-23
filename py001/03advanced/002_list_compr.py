#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=============1. python列表生成器======================
print("使用 [表达式 for循环迭代 过滤条件] 的形式，进行列表的生成")

#例如, [x if x % 2 == 0 else -x for x in range(1, 11)] => [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
# 其中x if x % 2 == 0 else -x 是表达式，for x in range(1, 11)是迭代
print(f"例如, [x if x % 2 == 0 else -x for x in range(1, 11)] => {[x if x % 2 == 0 else -x for x in range(1, 11)]}")

# 例如, [x * x for x in range(1, 11) if x % 2 == 0] => [4, 16, 36, 64, 100]
# 其中，x * x是表达式， for x in range(1, 11)是迭代，if x % 2 == 0是过滤条件
print(f"例如, [x * x for x in range(1, 11) if x % 2 == 0] => {[x * x for x in range(1, 11) if x % 2 == 0]}")

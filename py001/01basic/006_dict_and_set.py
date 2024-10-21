#!/usr/bin/env python
# -*- coding: utf-8 -*-

#======================python中的字典dict，其他语言称为map==============================
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
v1 = d['Michael']
print(f"Dict: find key MichaelOrignal => {v1}")

d['Michael'] = 100
v2 = d['Michael']
print(f"Dict: find key MichaelNew => {v2}")

# 判断key是否在dict中
if 'Thomsa' in d:
    print("Yes")

# 删除字典中的一个key
d.pop('Bob')

#======================python中的集合Set, 可以理解为value都为""的dict===================
s1 = {1, 3, 5, 7, 9}
# 通过list快速转换为set
s2 = set([2, 4, 6, 8, 10])

# 通过add方法，追加元素到set中
s1.add(100)
s2.add(100)

# 通过remove方法，可以删除集合中的元素
s1.remove(1)
s2.remove(2)

# 集合求交集
s3 = s1 & s2
print(f"两集合取交集s1 & s2: {s3}")

# 集合求并集
s4 = s1 | s2
print(f"两集合取并集s1 | s2: {s4}")

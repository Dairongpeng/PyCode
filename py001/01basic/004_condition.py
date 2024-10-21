#!/usr/bin/env python
# -*- coding: utf-8 -*-

# =====================================条件判断========================================
s = input('请输入你的年龄: ')
age = int(s)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#=========================match判断类似其他语言的switch-case========================

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

#==========================函数定义使用def关键字=================================
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

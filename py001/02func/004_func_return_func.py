#!/usr/bin/env python
# -*- coding: utf-8 -*-

#======================1. 函数可以作为返回值返回（闭包）============================
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 此时返回了f, lazy_sum并没有执行具体的加和运算
f = lazy_sum(1, 3, 5, 7, 9)

# 当函数返回一个函数时候，需要执行的地方运行这个函数，才会得到真正的执行，f是lazy_sum的函数返回，f() => 25
print(f"当函数返回一个函数时候，需要执行的地方运行这个函数，才会得到真正的执行，f是lazy_sum的函数返回，f() => {f()}")


#====================================2. 匿名函数========================================
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。例如：lambda x: x * x等价于
def(x):
    return x * x

f1 = lambda x: x * x

# lambda x: x * x, f(5) = > 25
print(f"lambda x: x * x, f(5) = > {f(5)}")

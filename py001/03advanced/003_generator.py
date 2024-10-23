#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=================1. python中的生成器，目的是节省内存，只有当调用next的时候，生成器才会加载一个元素到内存===============
# 在上一节，列表生成器是通过[表达式 迭代 筛选条件]来生成的，而生成器，则是通过(表达式 迭代 筛选条件)来生成，区别就在括号上
# generator本质保存的是算法，是获取下一个元素的算法next。每次调用next获取下一个元素值，直到最后一个元素值
# generator是可迭代对象，直接迭代可以省去next的调用, 也不用关心结束迭代器标记StopIteration

g = (x * x for x in range(10))
for n in g:
     print(f"生成器获(x * x for x in range(10))取到了当前元素n => {n}")

#=================2. 除了根据条件获得生成器，还可以自己定义生成器函数====================
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

# 拿到/初始化一个新的生成器generator
o = odd()
# 每次调用next(o)获取yield返回
#step 1
#step 2
#step 3
next(o)
next(o)
next(o)

# 生成器改在fib的例子
#fib(6), cur x:, x)
#fib(6), cur x:, x)
#fib(6), cur x:, x)
#fib(6), cur x:, x)
#fib(6), cur x:, x)
#fib(6), cur x:, x)
#Generator return value: done
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)
while True:
    try:
        x = next(g)
        print('fib(6), cur x:, x)')
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
# generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
# 请注意区分普通函数和generator函数，普通函数调用直接返回结果, generator函数的调用实际返回一个generator对象

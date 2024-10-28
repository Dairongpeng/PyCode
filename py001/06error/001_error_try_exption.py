#!/usr/bin/env python

#=======================1. python中的错误捕获===========================
# try-except-finally机制，finally无论有没有发生异常，都会执行

# try...
# except: division by zero
# finally...
# END
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# python中错误捕获可以跨层级。比如main调用a，a调用b，b发生异常，name在，main中也是可以捕获得到的。

#========================2. python中记录错误=============================
# python内置的logging模块可以非常容易记录错误信息。打印完错误后，可以继续执行，并正常退出

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

#=======================3. python中抛出错误===============================
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

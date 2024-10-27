#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=================1. 使用模块=========================
# python模块分为内置模块和外部模块，内置模块是在标准库的，可以直接使用，外部模块需要事先安装

# 模块的文档注释写在这里
'a test module'

# 模块的作者，写在这里
__author__ = 'dairongpeng'

import sys

def test():
    # args保存了命令行的所有参数，什么参数没有，这里也会至少一个参数是.py文件的名称
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 当我们在命令行运行该模块时，python解释器会把特殊变量__name__置为__main__, 而其他地方导入该模块，这个判断会失效
if __name__=='__main__':
    test()


#=================2. 模块中的变量========================
# 公开变量，对模块外调用公开的变量，就是正常的书写就可以，包括函数名，变量名，类名等
# 特殊变量，类似__xxx__，这样的变量可以被直接引用，但是有特殊用途
# 私有变量，类似_xxx, __xxx，这样的函数或者变量，是私有的，不应该被模块外直接引用到


def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)






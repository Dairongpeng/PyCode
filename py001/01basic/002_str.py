#!/usr/bin/env python
# -*- coding: utf-8 -*-


print('===========================1. Python中的字符入门===========================')

print('Python使用UTF-8编码字符串')

print("ord()函数获取字符的整数表示，例如ord('中')=", ord('中'))

print("chr()函数获取编码对应的字符，例如chr(66)=", chr(66))

print('====================2. Python中的字符串与字节数组转换======================')

print("字符串转换字节数组bytes使用.encode()方法，例如'你好'.encode('utf-8')=", '你好'.encode('utf-8'))

print("字节数组bytes也叫做字节流，字节流转换为字符串使用.decode()方法，例如b'\\xe4\\xb8\\xad\\xe6\\x96\\x87'.decode('utf-8')=", b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print("字符串使用len()函数是查询字符串含有字符数，例如len('中文')=", len("中文"), "字节流数组bytes使用len()函数是查询字节数，例如len('中文'.encode('utf-8'))=", len('中文'.encode('utf-8')))

print("一般的，为了让python解释器一直能够按照utf8读取源代码，我们常常在源代码的开头增加-*- coding: utf-8 -*- 标识")

print("==========================3. 字符串的格式化================================")

print("python中最常用的格式化是使用f-strings方式, 例如f'Name: {name}, Age: {age}', 其中{name}和{age}是需要填充的占位符")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#从列表起始位置方向切片，例子['Michael', 'Sarah', 'Tracy'][0:1] => ['Michael']
print(f"从列表起始位置方向切片，例子['Michael', 'Sarah', 'Tracy'][0:1] => {['Michael', 'Sarah', 'Tracy'][0:1]}")

#从列表结束位置方向切片，例子['Michael', 'Sarah', 'Tracy'][-2:-1] => ['Sarah']
print(f"从列表结束位置方向切片，例子['Michael', 'Sarah', 'Tracy'][-2:-1] => {['Michael', 'Sarah', 'Tracy'][-2:-1]}")

#元组切片和列表切片同理，例子(0, 1, 2, 3, 4)[:3] => (0, 1, 2)
print(f"元组切片和列表切片同理，例子(0, 1, 2, 3, 4)[:3] => {(0, 1, 2, 3, 4)[:3]}")

#字符串是可以看作字符数组也存在切片，例子'ABCDEFG'[:3] => ABC
print(f"字符串是可以看作字符数组也存在切片，例子'ABCDEFG'[:3] => {'ABCDEFG'[:3]}")

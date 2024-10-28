#!/usr/bin/env python

#========================1. string io=====================================
#很多时候，读写数据目标并非文件，也可以在内存中读写。

from io import StringIO

f = StringIO()

f.write('hello')
f.write(' ')
f.write('world!')

print(f"从stringIO中读取全部数据f.getvalue() => {f.getvalue()}")

# 使用StringIO, 对一个str进行初始化
f1 = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = f1.readline()
    if s == '':
        break
    print(f"从StringIO中按行读取 => {s.strip()}")


#========================2. bytes io======================================
# string io只能操作str的流，如果要操作二进制流，应该使用BytesIO。
from io import BytesIO

f2 = BytesIO()
# 这里写入的时经过utf-8编码后的bytes
f2.write('中文'.encode('utf-8'))
print(f"从bytesIO中读取数据全部f2.getvalue() => {f2.getvalue()}")

# 按行和按chunk读取，类似

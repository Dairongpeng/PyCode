#!/usr/bin/env python

#===========================1. python操作系统相关命令================================
import os

# 可以查看操作系统类型，posix为Unix和类Unix。nt是win
os.name

# 可以查看更为详细的系统信息
os.uname()

# 查看系统环境变量
os.environ

# 获取某个key对应的环境变量值
os.environ.get('key')

# 查看当前目录的绝对路径
os.path.abspath('.')

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来，使用join可以省去关系操作系统分隔符的差异:
p = os.path.join('/home/dairongpeng', 'testdir')
# 接着创建
os.mkdir('/home/dairongpeng/testdir')
# 删除一个目录
os.rmdir('/home/dairongpeng/testdir')

# 要拆分路径时，同样的，使用os.path.split()，不用关心操作系统分隔符差异。使用split，最后一部分总是最后一级的目录或者文件，os.path.splitext()拆分可以直接获取最后一级文件的扩展名
# ('/Users/michael/testdir', 'file.txt')
os.path.split('/home/dairongpeng/testdir/file.txt')

# 文件重命名
os.rename('test.txt', 'test.py')

# 删掉文件
os.remove('test.py')

# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]

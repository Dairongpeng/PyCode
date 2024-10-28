#!/usr/bin/env python

#==============================1. python IO之读写文件===================================

#==================================1. 读取文件========================================
#读文件：以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符, 标示符'r'表示读
f1 = open('/home/dairongpeng/test.txt', 'r')

# 如果文件打开成功，调用read()方法可以一次读取文件的全部内容到内存，用一个str对象表示
text = f1.read()

# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f1.close()

# 通常为了保证读写文件的过程总，文件总是会正常close，可以使用try-finally，close放到finally内
try:
    f2 = open('/home/dairongpeng/test.txt', 'r')
    print(f"try一次性读取文件 => {f2.read()}")
finally:
    if f2:
        f2.close()

# 上述这么写，是可以但是太繁琐，python简化了这种书写，使用with，总是会保证文件会被close，等价于上述try-finally
with open('/home/dairongpeng/test.txt', 'r', encoding='utf-8') as f3:
    print(f"with一次性读取文件 => {f3.read()}")

f4 = open('/home/dairongpeng/test.txt', 'r')

# 防止一次读取文件到内存，负担过重，可以按行读取
for line in f4.readlines():
    print(f"按行读取文件 => {line.strip()}") # 把末尾的'\n'删掉

# 防止一次读取文件到内存，负担过重，可以按照chunk读取
def read_file_in_chunks(file_path, chunk_size):
    with open(file_path, 'rb') as file:  # 以二进制模式打开文件
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk  # 使用 yield 生成器来逐块返回数据

# 示例使用
file_path = '/home/dairongpeng/test.txt'
chunk_size = 1024  # 每次读取 1024 字节

for chunk in read_file_in_chunks(file_path, chunk_size):
    # 处理每个块，例如打印块内容
    print(f"按照chunk读取 => {chunk}")

#======================================2. 写文件=======================================
# 写文件和读文件类似，open时，传入w或者wb，wb是按照二进制写入
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
f5 = open('/home/dairongpeng/test1.txt', 'w')
print("open一次性覆盖写入文件test1.txt")
f5.write('Hello, world!')
f5.close()

# 同样的，为了防止忘记书写close，可以使用with
with open('/home/dairongpeng/test1.txt', 'w') as f6:
    print("with一次性覆盖写入文件test1.txt")
    f6.write('Hello, world!')

# 写文件是，如果是w或者wb模式写入，对应是replace操作，替换掉原来已经存在的文件。如果希望追加写，可以使用'a'模式

#!/user/bin/env python

import types

#======================1. 类实例对象的信息==============================
# python中可以使用type函数，来判断对象的类型
#整数123的的类型type(123) => <class 'int'>
print(f"整数123的的类型type(123) => {type(123)}")

# 字符串‘str’的的类型type('str') => <class 'str'>
print(f"字符串‘str’的的类型type('str') => {type('str')}")

# type函数返回的类型为Class类型。标准库types中定义了许多类型常量

def fn():
    pass

# 函数fn类型，是否等于types.FunctionType，True
print(f"函数fn类型，是否等于types.FunctionType，{type(fn)==types.FunctionType}")

# 能用type判断类型的对象，基本都可以用isinstance()函数判断，一般的判断一个实例是否是某个类的类型，用isinstance()

# True
isinstance('a', str)

# True
isinstance([1, 2, 3], (list, tuple))


# object -> Animal -> Dog
class Animal(object):
    pass

class Dog(Animal):
    pass

a = Animal()
d = Dog()

# dog实例是不是Dog类的类型 => True
print(f"dog实例是不是Dog类的类型 => {isinstance(d, Dog)}")
# ... True
print(f"animal实例是不是Animal类型 => {isinstance(a, Animal)}")
# ... True
print(f"dog实例是不是Animal类型 => {isinstance(d, Animal)}")


#=================================2. 获取对象的所有信息dir()=================================
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
# 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 
# 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 
# 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(f"或许字符串ABC的所有属性 => {dir('ABC')}")

# 当调用len函数，试图获取字符串长度时，实际上下面两种等价的
len('ABC')

'ABC'.__len__()

# 我们自己自定义的类，如果也想直接使用len函数，只需要定义Class的时候，定义__len__方法即可
class MyC(object):
    def __len__(self):
        return 100


mc = MyC()
# 自定义类调用len => 100
print(f"自定义类调用len => {len(mc)}")


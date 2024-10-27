#!/user/bin/env python
# -*- coding: utf-8 -*-

#===========================1. python中的继承多态=============================

# 定义base class基类Animal
class Animal(object):
    def run(self):
        print('Animal is running...')

# 子类sub class继承了基类Animal
class Dog(Animal):
    pass

# 对于Dog和Cat来说，继承自Animal，天然拥有了run方法
dog = Dog()
# Animal is running...
dog.run()

# 子类可以重写父类的方法，实现多态
class Cat(Animal):
    def run(self):
        print('Cat is running...')

# 要判断变量是否属于某个类型可以用isinstance()判断
cat = Cat()
cat.run()
# true
isAnimal = isinstance(cat, Animal)
# cat is animal? => True
print(f"cat is animal? => {isAnimal}")

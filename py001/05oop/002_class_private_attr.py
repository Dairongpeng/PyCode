#!/user/bin/env python
# -*- coding: utf-8 -*-

# 私有化类的属性可以通过在属性前，增加__来实现

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 定义给外部实例变量，获取私有__name变量的方法
    def get_name(self):
        return self.__name

    # 定义给外部实例变量，获取私有__name变量的方法
    def get_score(self):
        return self.__score

    # 定义给外部修改私有变量__score的方法
    def set_score(self, score):
        self.__score = score

bart = Student('Bart Simpson', 59)

# 通过外部，即实例，再去访问变量，就不允许了，只能通过类提前为实例定义的方法，来操作属性
# bart.__name  会报错


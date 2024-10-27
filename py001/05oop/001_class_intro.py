#!/usr/bin/env python
# -*- coding: utf-8 -*-

#============================1. 类的介绍与定义==============================

# Student是类名，类名通常首字母大写，类是抽象的一个模板。参数表示类是由哪个类继承下来的，object是所有类的父类
class Student(object):
    # 这是class实体Student的构造函数，这个初始化构造方法，注意前后有__下划线，第一个参数永远是self, self就表示即将
    # 创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 这是class实体提供的类方法，与普通函数不同，类中的方法，第一个参数必须是实例变量self，且调用的时候不用传递该参数
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 默认调用到Student的构造方法，构造出来一个类实例Instance。创建实例通过类名+(),括号内可带参数可不带
# 取决于，类中有没有__init__方法，如果有，必须传相对应的，不能传空，self不需要传
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

# 实例Instance可以直接调用类方法
bart.print_score()
lisa.print_score()

#=============================2. 类的数据封装======================================
# 通过类的方法，封装数据。从Student类来看，创建一个实例需要name和score。类定于了绑定到实例上的方法print_score
# 该方法可以直接访问实例的数据。通过在实例上调用该方法，无需知道方法内部细节。
# 实例实例化后，可以增加自己的属性，例如bart = Student('Bart Simpson', 59)，指定了name和score，还可以bart.age=18，
# 增加实例自身的属性

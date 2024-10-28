#!/usr/bin/env python

#===========================1. python slots===========================
# 当我们从一个类实例化一个实例后，可以为该实例增加属性，和实例方法。当前实例绑定的属性和方法，不影响其他实例。
# 如果希望为所有实例绑定方法，可以给class绑定方法。class上绑定的属性方法，所有实例都可以使用。
# 限制实例属性，可以使用__slots__变量

# 只允许该类，添加name和age属性，添加其他属性会报错
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

# slots的限制，只对当前类的实例有效，对其集成的子类实例，无效。

#===========================2. python property=========================
# Python内置的@property装饰器就负责把一个方法变成属性调用。

class Student(object):
    # 加上@property后，就可以通过属性调用达到getter的效果
    @property
    def score(self):
        return self._score

    # 上面property加上后，自动会生成下面的装饰器，对setter进行属性调用
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # 这里的属性调用，对应的就是s.set_score(60)
s.score # 这里的属性调用，对应的就是s.get_score()

# property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

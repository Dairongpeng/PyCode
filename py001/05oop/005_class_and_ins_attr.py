#!/user/bin/env python

#=======================1. 实例属性及类属性==================================
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
# 为实例绑定一个属性score，称为实例属性
s.score = 90

# 类属性是通过class定义时绑定, 类属性，归类所有，但是所有实例对象，都可以访问的到
class Student1(object):
    name = 'Student1'

# 创建一个实例s
s = Student1()

print(f"实例s从类继承到了name属性，s.name = > {s.name}")

print(f"直接获取类的属性打印，Student1.name => {Student1.name}")

s.name = 'AAA'

print(f"实例属性比类属性优先级高，s.name => {s.name}")

# 清空实例的属性后，再访问实例的name，就会访问得到类的属性name了
del s.name

print(f"清空实例属性后，再次访问name，访问到类的属性，s.name => {s.name}")



#!/usr/bin/env python

#=============================1. python json序列化反序列化==================================
import json
d = dict(name='Bob', age=20, score=88)
# dumps()方法返回一个str，内容就是标准的JSON
# '{"age": 20, "score": 88, "name": "Bob"}'
json.dumps(d)

# dump()方法也可以直接把JSON写入一个file-like Object。也可以是流
f = open('dump.txt', 'wb')
json.dump(d, f)

# JSON反序列化为Python对象，用loads()或者对应的load()方法
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# {'age': 20, 'score': 88, 'name': 'Bob'}
json.loads(json_str)

# 如何对Python中的类进行序列化？
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

# 先把class转换为dict，再序列化
# {"age": 20, "name": "Bob", "score": 88}
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

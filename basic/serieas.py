#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#序列化
#一旦程序结束，变量所占用的内存就被操作系统全部回收
d = dict(name='Bob', age=20, score=88)
#把变量从内存中变成可存储或传输的过程称之为序列化

import pickle
print(pickle.dumps(d))  #把任意对象序列化成一个bytes

#直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，
# 然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

print('****************json**************')
#json
#把Python对象变成一个JSON
d = dict(name='Bob', age=20, score=88)
import json
print(json.dumps(d))

#把JSON反序列化为Python对象，用loads()或者对应的load()方法
#前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

#JSON进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
#之所以无法把Student类实例序列化为JSON，是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
#可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可
def changeStu(stu):
    return {
        'name':stu.name,
        'age':stu.age,
        'score':stu.score
    }
s = Student('chen',18,100.56)
print(json.dumps(s,default=changeStu))
#下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
print(json.dumps(s,default=lambda s : s.__dict__))

#json反序列成Student实例
def dict_Student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict_Student))

obj = dict(name='小明', age=20)
print(json.dumps(obj, ensure_ascii=False))









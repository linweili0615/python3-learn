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










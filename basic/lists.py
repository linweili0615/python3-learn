#/usr/bin/env python3
#coding=utf-8
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
#列表元素个数
print(len(classmates))
#索引来访问list
print(classmates[0])
print(classmates[1])
#最后一个元素的索引是len(classmates) - 1
print(classmates[len(classmates)-1])
print(classmates[-1])
#list添加元素
classmates.append('test')
print(classmates[-1])
#要删除list末尾的元素
classmates.pop()
print(classmates[-1])
#删除指定位置的元素
classmates.pop(-1)
print(classmates[-1])
#替换成别的元素
classmates[-1] = 'test'
print(classmates)
#list里面的元素的数据类型也可以不同
classmates.append(True)
print(classmates[-1])
s = ['python', 'java', ['asp', 'php'], 'scheme']
s.insert(1,'tt')
print(s[1])
print(s[2][1])

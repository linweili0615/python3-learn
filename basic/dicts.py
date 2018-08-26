#/usr/bin/env python3
#coding=utf-8
#使用键-值（key-value）存储
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('Thomas' in d)
print('Bob' in d)
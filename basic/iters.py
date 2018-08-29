#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
#dict迭代的是key。如果要迭代value
for value in d.values():
    print(value)

#同时迭代key和value
for k, v in d.items():
    print(k,v)

#判断一个对象是可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

#enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(print(i, value))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)
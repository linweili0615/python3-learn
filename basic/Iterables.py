#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#迭代器
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('',Iterable))
print(isinstance((x for x in range(100)),Iterable))

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
from collections import Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

for x in [1, 2, 3, 4, 5]:
    pass

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


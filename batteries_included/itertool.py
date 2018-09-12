#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
#cycle()会把传入的一个序列无限重复下去
# cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
# for c in cs:
#     print(c)

#repeat()负责把一个元素无限重复下去
# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

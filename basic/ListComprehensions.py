#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#内存限制
#列表生成式受到内存限制，列表容量肯定是有限的
#生成1~11
# range(1, 11)
#返回迭代对象
# for x in range(1, 11)

print(list(x * x for x in range(1, 11)))

print(list(x * x for x in range(1, 11) if x % 2 ==0))

#使用两层循环，可以生成全排列
print(list(m + n for m in 'ABC' for n in 'XYZ'))

import os
#os.listdir可以列出文件和目录
print(list(d for d in os.listdir('.')))
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print(list([k + '=' + v for k, v in d.items()]))

#把一个list中所有的字符串变成小写
L = ['Hello', 'World',66, 'IBM', 'Apple']
# print(list(s.lower() for s in L))

#1、使用内建的isinstance函数可以判断一个变量是不是字符串
# 2、s.lower() 可以将一个大写字母转为小写。
# 3、增加if语句保证列表生成式正确执行。

print(list(s.lower() if isinstance(s,str) else s for s in L))

print(list(m + n for m in 'ABCD' for n in 'XYZ'))
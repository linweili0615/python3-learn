#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#map
def f(x):
    return x * x
#map()作为高阶函数，事实上它把运算规则抽象
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
#把这个list所有数字转为字符
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#reduce
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#对一个序列求和
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1,3,5,7,9]))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int('13579'))
#lambda函数进一步简化成
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('13579'))

#首字母大小
# def normalize(s):
#     return s.capitalize()

def normalize(n):
    return n[:1].upper() + n[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#接受一个list并利用reduce()求积
def prod(lists):
    return reduce(lambda x,y: x * y, lists)

print(prod([3,5,7,9]))

print(3*5*7*9)

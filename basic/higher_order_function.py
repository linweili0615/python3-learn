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
print('------------------------------')
#和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1,3,4,5,6,78,9])))

#关键在于正确实现一个“筛选”函数
#返回2以上的素数
#取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
#
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
#
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(lambda x : x % n >0, it)
#调用时需要设置一个退出循环的条件
for p in primes():
    if p < 1000:
        print(p)
    else:
        break

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数


#反转字符串
def revearse(s):
    s = str(s)
    return s == s[::-1]

print(list(filter(revearse, range(1,1000))))

print(list(filter(lambda n : str(n) == str(n)[::-1], range(1,1000))))


#sorted排序
#对list排序
print(sorted([36,30,-9,7,-10]))
#可以接收一个key函数来实现自定义的排序
print(sorted([36,30,-9,7,-10],key=abs))
#反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda x:x[0]))
print(sorted(L, key=lambda x:x[1]))







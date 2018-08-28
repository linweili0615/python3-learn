#/usr/bin/env python3
#coding=utf-8

#绝对值abs函数
print(abs(-20))
#max()可以接收任意多个参数，并返回最大的那个
print( max(2, 3, 1, -5))
#int()函数可以把其他数据类型转换为整数
print(int('123'))
print(float('12.34'))
print(str(1.23))
print(bool(1))
print(bool(''))
#空函数
def nop():
    pass

def func(x):
    if x > 0:
        print(True)
    else:
        print(False)

func(9)

#对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def validate(x):
    if not isinstance(x,(int,float)):
        print('类型不正确')
    else:
        print('x: %s' % x )

validate(['fds','fsd'])

import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2,10))
#默认参数
#必选参数在前，默认参数在后，否则Python的解释器会报错
def pow(x, n=10):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(pow(2))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah', 'F')
enroll('Adam', 'M', city='Tianjin')
#定义默认参数要牢记一点：默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print( add_end())
print( add_end())







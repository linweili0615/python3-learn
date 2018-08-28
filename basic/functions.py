#/usr/bin/env python3
#coding=utf-8
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

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

#可变参数
#允许你在list或tuple前面加一个*号
def calc(*numbers):
    #参数numbers接收到的是一个tuple
    #传入任意个参数，包括0个参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc())
print(calc(1,2,3))
print(calc(*[1,2,3]))

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
#简化写法
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


#命名关键字参数
#检查传入参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
#限制关键字参数的名字，就可以用命名关键字参数
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person0(name, age, *, city, job):
    print(name, age, city, job)
person0('Jack', 24, city='Beijing', job='Engineer')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
def person1(name, age, *args, city, job):
    print(name, age, args, city, job)

# person1('Jack', 24, 'Beijing', 'Engineer')

#命名关键字参数可以有缺省值。调用时，可不传入city参数
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person3('Jack', 24, job='Engineer')

#参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)







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











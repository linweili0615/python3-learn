#/usr/bin/env python3
#coding=utf-8
#递归函数/过多调用会导致栈溢出
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
fact(5)
#递归调用的次数过多，会导致栈溢出
# fact(1000)

#尾递归优化
def fact1(n):
    return fact_iter(n, 1)

#return fact_iter(num - 1, num * product)仅返回递归函数本身，
# num - 1和num * product在函数调用前就会被计算，不影响函数调用
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
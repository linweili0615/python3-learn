#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#生成器
#一边循环一边计算的机制，称为生成器：generator
#只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))

#通过for循环来迭代它，并且不需要关心StopIteration的错误
for n in g:
    print(n)

my_gen_01 = (i*2 for i in range(10))
"""
可以看到my_gen是一个generator对象
"""
print(my_gen_01)  # <generator object <genexpr> at 0x00000000024FCBA0>
#   generator对象是一个迭代器对象，所以直接通过next()方法来迭代
while True:
    try:
        print(next(my_gen_01))     # 迭代（根据公式计算）
    except StopIteration as e:  # 迭代到没有元素后会抛出StopIteration
        print(e.value)
        break



#"""函数运行到yield的时候，就会暂停，并将yield关键字之后的值传到函数外，函数暂停在这里，直到等到下一次迭代"""
def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        a, b = b, a+b
        n += 1


# 定义了一个生成器，这个生成器每次迭代得到的值就是yield带出来的值


fb = fib(10)

#  用for循环迭代
for val in fb:
    print(val)


# 用next迭代
fb1 = fib(10)
while True:
    try:
        print(next(fb1))
    except StopIteration as e:
        print(e.value)
        break

#yield能带出函数中的值，那么yield就是函数内部与外界的媒介，那么自然也能从外部代值回来：
def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        xxx = yield b  # 后面的b在运行到yield时被带出去，前面的xx在激活yield时被带进来
        print(xxx)
        a, b = b, a+b
        n += 1
    return 'done'



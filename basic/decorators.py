#/usr/bin/env python3
#coding=utf-8

#代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def now():
    print('2015-3-25')

print(now.__name__)

def log(func):
    def wrapper(*args,**kwargs):
        print('call %s(): (%s,%s)' % (func.__name__, args, kwargs))
        return func(*args,**kwargs)
    return wrapper
@log
def test(*args,**kwargs):
    print(1)

test(*(1,2,3),**{'kk':'ee','jj':33})

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def log1(text):
    def decotators(func):
        def wrapper(*args,**kwargs):
            print('%s call %s(): (%s,%s)' % (text,func.__name__, args, kwargs))
            return func(*args,**kwargs)
        return wrapper
    return decotators

@log1('test')
def test1(*args,**kwargs):
    print(1)

test1()
print(test1.__name__)
#经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'

import functools

def log2(text):
    def decotators(func):
        #如果想要保留原函数的属性，就可以用到functools.wraps了
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s call %s(): (%s,%s)' % (text,func.__name__, args, kwargs))
            return func(*args,**kwargs)
        return wrapper
    return decotators

@log2('test')
def test2(*args,**kwargs):
    print(1)

print(test2.__name__)

#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def logs(func):
    def wrapper(*args,**kwargs):
        print('start call %s' % func.__name__)
        c = func(*args,**kwargs)
        print('end call %s' % func.__name__)
        return c
    return wrapper
@logs
def test3(*args,**kwargs):
    print(1)


test3()
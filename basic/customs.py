#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#原因是__getitem__()传入的参数可能是一个int，
# 也可能是一个切片对象slice，所以要做判断

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    #要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，
    # 那就是写一个__getattr__()方法，动态返回一个属性
    #当调用不存在的属性时，比如score，
    # Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
    def __getattr__(self, attr):
        if attr == 'score':
            return 99

#但是没有对step参数作处理
#此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素

#利用完全动态的__getattr__，我们可以写出一个链式调用
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    #任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self):
        print('My _path is %s.' % self._path)

print(Chain().status.user.timeline.list)
c = Chain('stp')
c()

#判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print(callable(Chain()))
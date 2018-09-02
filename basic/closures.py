#/usr/bin/env python3
#coding=utf-8
#闭包Closure
#我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
f1 = lazy_sum(1,3,5,7,9)
print(f())

#每次调用都会返回一个新的函数，即使传入相同的参数
print(f == f1)

#返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1(),f2(),f3())
#全部都是9！原因就在于返回的函数引用了变量i，
# 但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

#缺点是代码较长，可利用lambda函数缩短代码
f1, f2, f3= [(lambda j = i : j ** 2) for i in range(1, 4)]
print(f1(),f2(),f3())




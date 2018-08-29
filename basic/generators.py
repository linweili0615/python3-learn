#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#生成器
#一边循环一边计算的机制，称为生成器：generator
#只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))

#通过for循环来迭代它，并且不需要关心StopIteration的错误
for n in g:
    print(n)


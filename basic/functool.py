#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#偏函数
print(int('12345'))
print(int('12345'))
def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))

import functools
s2 = functools.partial(int,base=2)
print(s2('10000'))
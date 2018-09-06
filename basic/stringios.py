#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

#要读取StringIO，可以用一个str初始化StringIO，
# 然后，像读文件一样读取
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

#BytesIO
#如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
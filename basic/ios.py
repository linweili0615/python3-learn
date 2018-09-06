#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#读文件
try:
    f = open('test.txt','r')
    print(f.read())
except  BaseException as e:
    raise
finally:
    f.close()


#引入了with语句来自动帮我们调用close()方法
with open('test.txt') as f:
    print(f.read())

#调用readline()可以每次读取一行内容，
# 调用readlines()一次读取所有内容并按行返回list
#如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open('test.txt') as f:
    for line in f.readlines():
        print(line.rstrip())

#二进制文件
f = open('test.jpg','rb')
print(f.read())

#字符编码
f = open('gbk.txt', 'r', encoding='gbk',errors='ignore')
print(f.read())

#写文件
#写文件和读文件是一样的，唯一区别是调用open()函数时，
# 传入标识符'w'或者'wb'表示写文本文件或写二进制文件

#以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
with open('text.txt','a') as f:
    f.write('hello kugou')
with open('text.txt','r') as f:
    print(f.read())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
#如果是posix，说明系统是Linux、Unix或Mac OS X，
# 如果是nt，就是Windows系统
print(os.name)  ## 操作系统类型
# print(os.uname()) #window不存在该参数
print(os.environ) #获取环境变量
print(os.environ.get('path'))

#操作文件和目录
#查看当前目录绝对路径
print(os.path.abspath('.'))
#返回新目录的完整路径
print(os.path.join('D:\PyProject\python3-learn\\basic','test'))
dir = os.path.join('D:\PyProject\python3-learn\\basic','test')
#创建文件夹
os.mkdir(dir)
#删除文件夹
os.rmdir(dir)

#拆分路径
#可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('D:\PyProject\python3-learn\\basic\\text.txt'))

#获取文件扩展名
print(os.path.splitext('D:\PyProject\python3-learn\\basic\\text.txt'))

#对文件重命名
# os.rename('D:\PyProject\python3-learn\\basic\gbk1.txt','D:\PyProject\python3-learn\\basic\gbk.txt')
#删除文件
# os.remove('test.py')

#复制文件
import shutil
# shutil.copy('D:\PyProject\python3-learn\\basic\\text.txt','D:\PyProject\python3-learn\\basic\\text1.txt')

dir_list = (x for x in os.listdir('.') if os.path.isfile(x))
# print(next(dir_list))
for d in dir_list:
    print(d)

#列出所有的.py文件
file_list = (x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py')
for fi in file_list:
    print(fi)













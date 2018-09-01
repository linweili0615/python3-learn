#/usr/bin/env python3
#coding=utf-8
#切片Slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前3个元素
print(L[0:3])
print(L[:3])  #第一个索引是0，可以省略
print(L[1:3]) #从索引1开始，取出2个元素出来

#取倒数第一个元素
print(L[-1])
print(L[-2:-1]) #倒数切片

L = list(range(100))  #创建一个0-99的数列
print( L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2]) #前10个数，每两个取一个
print(L[::5])  #所有数，每5个取一个
print(L[:])  #只写[:]就可以原样复制一个list


#反转字符串
#切片法
def reverse1():
    s=input("请输入需要反转的内容：")
    return s[::-1]


#tuple、str 同上

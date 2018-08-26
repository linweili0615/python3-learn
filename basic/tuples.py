#/usr/bin/env python3
#coding=utf-8

#tuple不可变
classmates = ('Michael', 'Bob', 'Tracy')
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)

#可变tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
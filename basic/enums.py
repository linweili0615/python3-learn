#/usr/bin/env python3
#coding=utf-8
#枚举
from enum import Enum,unique
Weekend = Enum('Weekend',('Mon','Tues','Wed','Thurs','Fri','Sat','Sun'))
for name,member in Weekend.__members__.items():
    print(name, '==>', member.value, '==>', member)

print(Weekend.Mon.value)

#@unique来帮助我们检查类中定义的枚举成员变量的值是否有重复的
@unique
class Week(Enum):
    sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Week.sun.value)
print(Week['sun'].value)
print(Week(0).value)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    pass

s = Student()
s.name = 'test' #动态给实例绑定一个属性
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s) #给实例绑定一个方法
s.set_age(25) #调用实例方法
print(s.age)

#给一个实例绑定的方法，对另一个实例是不起作用的

#给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score
#给class绑定方法后，所有实例均可调用
s.set_score(66)
print(s.score)
s2 = Student()
s2.set_score(77)
print(s2.score)


#为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Engineer(object):
    __slots__ = ('name','age')
e = Engineer()
e.name = 'test'
print(e.name)
e.age = 69
print(e.age)
# e.score = 99
# print(e.score)

#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Trainee(Engineer):
    pass

t = Trainee()
t.score = 99
print(t.score)

#除非在子类中也定义__slots__，
# 这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Traineers(Engineer):
    __slots__ = ('score')

tt = Traineers()
tt.age = 55
print(tt.age)

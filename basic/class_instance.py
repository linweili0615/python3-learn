#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#类 -》 实例 -》 对象
#类可以起到模板的作用
class Student(object):
    #可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
    #在创建实例的时候，就把name，score等属性绑上
    #第一个参数永远是self，表示创建的实例本身
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_args(self):
        print('%s %s' % (self.name,self.score))

bart = Student
print(bart)
print(Student)
#可以自由地给一个实例变量绑定属性
bart.name = 'test123'
print(bart.name)

bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)

#数据封装
#Student实例本身就拥有这些数据，要访问这些数据，
# 就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数
tt = Student('test','123')
tt.print_args()

#访问限制
#以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Teacher(object):
    #可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
    #在创建实例的时候，就把name，score等属性绑上
    #第一个参数永远是self，表示创建的实例本身
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_args(self):
        print('%s %s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        #可以对参数做检查，避免传入无效的参数
        self.__score = score
#但是如果外部代码要获取name和score怎么办？可以给Teacher类增加get_name和get_score这样的方法

t1 = Teacher('tt','369')
t1.print_args()
#Python解释器对外把__name变量改成了_Student__name
print(t1._Teacher__name)
t1.__name = 'test666'
#实际上这个__name变量和class内部的__name变量不是一个变量



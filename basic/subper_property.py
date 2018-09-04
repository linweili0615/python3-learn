#/usr/bin/env python3
#coding=utf-8
#@property装饰器就是负责把一个方法变成属性调用的
class Student(object):
    @property
    def score(self):
        return self.score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('参数格式不对')
        if value < 0 or value > 100:
            raise ValueError('请输入0~100间的数字')


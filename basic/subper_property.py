#/usr/bin/env python3
#coding=utf-8
#@property装饰器就是负责把一个方法变成属性调用的
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


    #birth是可读写属性，而age就是一个只读属性
    @property
    def birth(self):
        return self._birth
    @property
    def age(self):
        return 2015 - self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value

        

s = Student()
s.score = 33
print(s.score)
# s.score = 101
# print(s.score)

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self.width = value



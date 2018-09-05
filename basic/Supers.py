#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#继承与多态
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def eat(self):
        print('Dog eating meat...')
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()
#多态
#当子类和父类都存在相同的run()方法时，
# 我们说，子类的run()覆盖了父类的run()，在代码运行的时候，
# 总是会调用子类的run()。这样，我们就获得了继承的另一个好处：
dog.run()
dog.eat()
cat.run()

def run_twice(animal):
    animal.run()
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())


#多层继承
class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print("woman")


class Child(Person):
    pass


class Baby(Child):
    pass


May = Baby("May", "female")  # 继承上上层父类的属性
print(May.name, May.sex)
May.print_title()  # 可使用上上层父类的方法


class Child(Person):
    def print_title(self):
        if self.sex == "male":
            print("boy")
        elif self.sex == "female":
            print("girl")


class Baby(Child):
    pass


May = Baby("May", "female")
May.print_title()  # 优先使用上层类的方法

#判断对象类型
print(type(May))

#判断一个对象是否是函数
import types
def fn():
    pass
print(type(fn) == types.FunctionType)

#判断class类型isinstance

#isinstance
#获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print( dir('ABC'))
print(len('ABC') == 'ABC'.__len__())

#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj,'x'))
print(obj.x)
setattr(obj,'y',6)
print(hasattr(obj,'y'))
print(obj.y)
## 获取属性'z'，如果不存在，返回默认值404
print(getattr(obj, 'z', 404) )
def readData():
    pass

#正确的用法的例子
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

#实例属性 和 类属性
#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    #直接在class中定义属性，这种属性是类属性
    name = 'Student'
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

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
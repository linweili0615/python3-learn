#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

global_dict = {}
def std_thread(name,age):
    std = Student(name,age)
    global_dict[threading.current_thread()] = std
    do_task1()
    do_task2()

def do_task1():
    print('do_task1(): %s' % threading.current_thread())
    std = global_dict[threading.current_thread()]
    print(std.name)
    print(std.age)
def do_task2():
    print('do_task1(): %s' % threading.current_thread())
    std = global_dict[threading.current_thread()]
    print(std.name)
    print(std.age)

if __name__ == '__main__':
    std_thread('test123',96)
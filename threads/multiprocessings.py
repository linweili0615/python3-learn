#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#多进程
import os
# print('Process %s start' % os.getpid())
# Only works on Unix/Linux/Mac:
# pid = os.fork()

#multiprocessing
from multiprocessing import Process
#下面的例子演示了启动一个子进程并等待其结束
def run_proc(name):
    print('run child process %s (%s)' % (name,os.getpid()))

if __name__ == '__main__':
    #创建子进程时，只需要传入一个执行函数和函数的参数，
    # 创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Parent Process %s' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process end')

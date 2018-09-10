#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, threading
def loop():
    print('thread %s is running' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s : %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=loop,name='loopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)

#多线程和多进程最大的不同在于，多进程中，同一个变量，
# 各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享

#假设金额
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    #先存后取，值应为0
    balance = balance +1
    balance = balance -1

def run_thread(n):
    for i in range(100):
        #获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            #最后必须要释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(6,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#多核CPU















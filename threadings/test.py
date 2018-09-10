#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys
import threading
import time

a = threading.local()

def my_thread(*args):
    while True:
        if args[0] == 1:
            a = 1
        elif args[0] == 2:
            a = 2
        print('[%s]: %d' % (threading.currentThread().getName(), a))


if __name__ == '__main__':
    t1 = threading.Thread(target = my_thread, args = (1,))
    t2 = threading.Thread(target = my_thread, args = (2,))

    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('[%s] Main thread finished' % threading.currentThread())
#/usr/bin/env python3
#coding=utf-8
import asyncio

# @asyncio.coroutine
# def hello():
#     print('Hello World')
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
# #获取eventloop
# loop = asyncio.get_event_loop()
# #执行coroutine
# loop.run_until_complete(hello())
# loop.close()
#
# import threading
#
# @asyncio.coroutine
# def hello1():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop1 = asyncio.get_event_loop()
# tasks = [hello1(), hello1()]
# loop1.run_until_complete(asyncio.wait(tasks))
# loop1.close()


import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()
#可见3个连接由一个线程通过coroutine并发完成。
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


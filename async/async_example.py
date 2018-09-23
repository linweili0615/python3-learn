#/usr/bin/env python3
#coding=utf-8
import asyncio, time

#定义第1个协程，协程就是将要具体完成的任务，该任务耗时3秒，完成后显示任务完成
async def to_do_something(i):
    print('第{}个任务：任务启动。。。'.format(i))
    #遇到耗时的操作，await就会将任务挂起，执行下一个任务
    await asyncio.sleep(2)
    print('第{}个任务：完成'.format(i))
#定义第2个协程，用于通知任务进行状态
async def missing_running():
    print('任务正在进行')

start = time.time()
#创建一个循环
loop = asyncio.get_event_loop()
#创建一个tasks任务盒子， 包含了3个需要完成的任务
tasks = [
    asyncio.ensure_future(to_do_something(1)),
    asyncio.ensure_future(to_do_something(2)),
    asyncio.ensure_future(missing_running())
]
#将tasks接入loop中运行
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(end - start)
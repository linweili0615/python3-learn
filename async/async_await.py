#/usr/bin/env python3
#coding=utf-8
import asyncio

# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#

# async def hello():
#     print("Hello world!")
#     r = await asyncio.sleep(1)
#     print("Hello again!")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


import asyncio
import aiohttp

url_lst_failed = []
url_lst_successed = []
async def get_info(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,timeout=5) as resp:
            if resp.status != 200:
                url_lst_failed.append(url)
            else:
                url_lst_successed.append(url)
            r = await resp.text()

get_info('https://www.baidu.com')
print(url_lst_failed)
print(url_lst_successed)

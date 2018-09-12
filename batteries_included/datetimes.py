#/usr/bin/env python3
#coding=utf-8
#获取指定日期和时间
from datetime import datetime
print(datetime.now())
print(datetime(2018,9,12,12,49))

#timestamp
#全球各地的计算机在任意时刻的timestamp都是完全相同的
print(datetime.now().timestamp())

#timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))    # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#datetime加减
from datetime import timedelta

now = datetime.now()
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

#本地时间转换为UTC时间

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
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

#时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#导入sqllite驱动
import sqlite3
#连接数据库db，不存在则创建
connect = sqlite3.connect('test.db')
#创建cursor
cursor = connect.cursor()
#执行sql，创建user表
import os
db_file = os.path.join(os.path.dirname(__file__), 'user.db')
if os.path.isfile(db_file):
    # os.remove(db_file)
    pass
else:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#插入数据
cursor.execute('insert into user (id, name) values ("2", "Michael")')
#通过rowcount获得插入的行数
print(cursor.rowcount)
values = cursor.fetchall()
print(values)
#关闭cursor
cursor.close()
#提交事务
connect.commit()
#断开连接
connect.close()
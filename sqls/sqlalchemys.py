#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

#创建对象的基类
Base = declarative_base()

#定义User对象
class User(Base):
    #表名字
    __tablename__ = 'user'
    #表的结构
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

#初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:123456a@localhost:3306/test')
#创建DBSession类型
DBSession = sessionmaker(bind=engine)
#创建session对象
session = DBSession()
#创建新User对象
# new_user = User(id='5', name='Bob')
#添加到session
# session.add(new_user)
#提交到数据库
# session.commit()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
print(user.id)
print(user.name)

from sqlalchemy.orm import class_mapper
def serialize(model):
    """Transforms a model into a dictionary which can be dumped to JSON."""
    # first we get the names of all the columns on your model
    columns = [c.key for c in class_mapper(model.__class__).columns]
    # then we return their values in a dict
    return dict((c, getattr(model, c)) for c in columns)

def to_json(self):
    columns = [c.key for c in class_mapper(self.__class__).columns]
    model_dict = dict((c, getattr(self, c)) for c in columns)
    return json.dumps(model_dict)

#将to_json方法添加到Base
Base.to_json = to_json

print(user.to_json())  #调用主类方法
print(to_json(user))

session.close()

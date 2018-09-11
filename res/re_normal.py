#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#   \d 匹配一个数字
#   \w 匹配一个字母或数字
#   .  匹配任意字符

#要匹配变长的字符
#   * 表示任意个字符（包括0个）
#   + 表示至少一个字符
#   \s 匹配一个空格(包括Tab等空白符)
#   \s+ 至少有一个空格
#   ? 表示 0 个或 1 个字符
#   {n} 表示 n 个字符
#   {n,m}   表示 n-m 个字符

# \d{3} \s+ \d{3,8}
#\d{3} 表示至少三个数字


#进阶
#   [] 表示范围
#   [0-9a-zA-Z\_]+  可以匹配至少由一个数字、字母或者下划线组成的字符串
#   [a-zA-Z\_][0-9a-zA-Z\_]*    可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量
#   [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}  更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
#   A|B 可以匹配    A或B
#   ^   表示行的开头，^\d 表示必须以数字开头。
#   $   表示行的结束，\d$ 表示必须以数字结束

#   使用Python的r前缀，就不用考虑转义的问题
s = r'ABC\-001'
import re
if re.match(r'^\w{3}\\-\d{3}',s):
    print('匹配成功')
else:
    print('匹配失败')

if re.match(r'^\d{3}\-\d{3,8}$', '010 12345'):
    print('ok')
else:
    print('bu ok')

#切分字符串
#识别连续的空格
print(re.split(r'\s+','ab  c'))
#至少一个空格或，或；切分
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

#分组
#()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

#贪婪匹配
#默认匹配尽可能多的字符
print(re.match(r'^(\d+)(0*)$', '102300').groups())
#加个?就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())


#预编译
re_ready = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_ready.match('010-12345').groups())

re_email = re.compile(r'^([\w\d\.\_]+)\@(\w+)([\.com|\.cn|\.org]+)$')

#校验email格式
def is_valid_email(email):
    if re_email.match(email):
        print('True: %s' % email)
        return True
    else:
        return False
#获取邮件名称
def get_email(email):
    return re_email.match(email).groups()

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')

print(get_email('mr_bob666@example.com'))
print(get_email('tom_12fds@voyager.org'))


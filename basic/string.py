#/usr/bin/env python3
#coding=utf-8

#字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，
# ''或""本身只是一种表示方式，不是字符串的一部分，因此，字符串'abc'只有a，b，c这3个字符。
# 如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。
#如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识

print('abc')
print("i'm abc")
print('she\'s \"abc\"')

#字符编码
print('中文')

#rd()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('字'))
print(chr(65))
print(chr(23383))
print('\u4e2d\u6587')

#bytes类型的数据用带b前缀的单引号或双引号表示
# str to bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

#bytes to str
print( b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

#字符长度
print(len('中文'))

#格式化
#%d	整数
#%f	浮点数
#%s	字符串
#%x	十六进制整数

#转义用%%来表示一个%

print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

#format()
print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
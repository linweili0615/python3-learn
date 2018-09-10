#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#子进程并不是自身，而是一个外部进程。
# 我们创建了子进程后，还需要控制子进程的输入和输出
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print(type(r))
# print('Exit code:', r)

import subprocess
#如果子进程还需要输入，则可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
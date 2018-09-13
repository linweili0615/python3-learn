#/usr/bin/env python3
#coding=utf-8
#email负责构造邮件，smtplib负责发送邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，
# 最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 输入Email地址和口令:
# from_addr = input('From: ')
# password = input('Password: ')
# 输入收件人地址:
# to_addr = input('To: ')
# 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
smtp_server = ''
from_addr = ''
password = ''
to_addr = ''

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()



import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)    #打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
##sendmail()方法就是发邮件，由于可以一次发给多个人，
# 所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
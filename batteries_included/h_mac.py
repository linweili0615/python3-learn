#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hmac
# bytes object
b = b"example"

# str object
s = "example"

# str to bytes
sb = bytes(s, encoding = "utf8")

# bytes to str
bs = str(b, encoding = "utf8")

# an alternative method
# str to bytes
sb2 = str.encode(s)

# bytes to str
bs2 = bytes.decode(b)

message = str.encode('Hello, world!')
key = str.encode('secret')
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
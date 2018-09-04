#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#多层继承
class RunableMixIn(object):
    def run(self):
        print('RunableMixIn running ...')
class FlyableMixIn(object):
    def fly(self):
        print('FlyableMixIn flying ...')

class Duck(RunableMixIn, FlyableMixIn):
    pass

d = Duck()
d.run()
d.fly()

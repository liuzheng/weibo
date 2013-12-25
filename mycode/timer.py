#!/usr/bin/env python
# coding: utf-8
# Copyright(c) 2013
# Gmail:liuzheng712
#

import sched
import time
import persion
import loginweibo as Lwb
import jiexi
import file

def write(session, who):
    page, who = Lwb.getPage(session, 'http://weibo.com/' + who)
    WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid = jiexi.detail(page)
    for i in range(0, len(WB_text)):
        file.inputweibo(who, WB_text[i], WB_time[i], WB_mid[i],
                WB_comefrom[i], WB_like[i], WB_forward[i], WB_pinlun[i])
    print 'Success!'

if len(persion.usename) == 0:
    username, passwd = Lwb.Login()
else:
    username = persion.usename
    passwd = persion.passwd
session = Lwb.getCookies(username, passwd)


scheduler = sched.scheduler(time.time, time.sleep)
#print time.time
#print time.sleep


def print_event(name):
    print 'EVENT:', time.time(), name

print 'START:', time.time()
for i in range(1, 86400):
    scheduler.enter(i, 1, write, (session, 'kaifulee'))

scheduler.run()

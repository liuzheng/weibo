#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#


from celery.task import task
import loginweibo as Lwb
import jiexi
import file

@task
def write(session, who):
    page, who = Lwb.getPage(session, 'http://weibo.com/' + who)
    WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid = jiexi.detail(page)
    for i in range(0, len(WB_text)):
        file.inputweibo(who, WB_text[i], WB_time[i], WB_mid[i],
                WB_comefrom[i], WB_like[i], WB_forward[i], WB_pinlun[i])
    print 'Success!'

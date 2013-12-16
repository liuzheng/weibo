#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#

import loginweibo as Lwb
import jiexi
import file

username, passwd = Lwb.Login()
session = Lwb.getCookies(username, passwd)
page, who = Lwb.PageOne(session)
WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid = jiexi.detail(page)
#jiexi.showweibo(WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward,
#        WB_mid)
for i in range(0, len(WB_text)):
    file.inputtxt(who, WB_text[i].lstrip('\\n').split(), WB_time[i], WB_mid[i],
            WB_comefrom[i], WB_like[i], WB_forward[i], WB_pinlun[i])


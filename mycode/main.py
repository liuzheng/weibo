#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#

import loginweibo as Lwb
import jiexi

username, passwd = Lwb.Login()
session = Lwb.getCookies(username, passwd)
page = Lwb.PageOne(session)
jiexi.detail(page)

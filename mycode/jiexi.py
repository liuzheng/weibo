#!/usr/bin/env python
# coding: utf-8
# Copyright(c) 2013
# Gmail:liuzheng712
#

import re
# from pyquery import PyQuery as pyq

content = open('index1.html').read()
# print html
# htm = pyq(content)
# pattern = re.compile(content)
# print htm.hasClass('PRF_modwrap')
# match = pattern.match('pl\.content\.homeFeed\.index')
# weibo = re.findall(r".*pl\.content\.homeFeed\.index.*", content)
#print weibo[0]
#single = re.findall(r"WB\_text[^>]*>([^<]*)<\\/div>", weibo[0])

# delete the forward weibo
tmp = re.findall(r'WB\_media\_expand SW\_fun2 S\_line1 S\_bg1\\">.*?WB\_func clearfix', content)
for tmp_r in tmp:
    content = content.replace(tmp_r, 's')

# get all things
WB_text = re.findall(r"WB\_text[^>]*>(.*?)<\\/div", content)
WB_time = re.findall(r'WB\_text[^>]*>.*?date=\\"([0-9]*)', content)
WB_comefrom = re.findall(r'WB\_text[^>]*>.*?nofollow\\">(.*?)<', content)
WB_like = re.findall(r'WB\_text[^>]*>.*?praised.*?\(([0-9]*)', content)
WB_pinlun = re.findall(r'WB\_text[^>]*>.*?fl_comment.*?\(([0-9]*)', content)
WB_forward = re.findall(r'WB\_text[^>]*>.*?fl_forward.*?>.*?\(([0-9]*)', content)

# print it
for i in range(0, len(WB_text)):
    print str(i+1) + '.' + WB_text[i].lstrip('\\n').strip()
    print 'time:' + WB_time[i]
    print 'comefrom:' + WB_comefrom[i]
    print 'like:' + WB_like[i]
    print 'forward:' + WB_forward[i]
    print 'pinlun:' + WB_pinlun[i]
#cts = htm('body')
#print cts

#for i in cts:
#    print '======', pyq(i).find('a').text(), '======'
#    for j in pyq(i).find('.sub'):
#        print pyq(j).text()
#    print '\n'

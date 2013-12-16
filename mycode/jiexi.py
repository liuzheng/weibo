#!/usr/bin/env python
# coding: utf-8
# Copyright(c) 2013
# Gmail:liuzheng712
#

import re


def detail(content):
    tmp = re.findall(r'WB\_media\_expand SW\_fun2 S\_line1 S\_bg1\\">.*?nofollow', content)
    for tmp_r in tmp:
        content = content.replace(tmp_r, 's')
    # get all things
    WB_text = re.findall(r"WB\_text[^>]*>(.*?)<\\/div", content)
    WB_time = re.findall(r'WB\_text[^>]*>.*?date=\\"([0-9]*)', content)
    WB_comefrom = re.findall(r'WB\_text[^>]*>.*?nofollow\\">(.*?)<', content)
    WB_like = re.findall(r'WB\_text[^>]*>.*?praised.*?\(([0-9]*)', content)
    WB_pinlun = re.findall(r'WB\_text[^>]*>.*?fl_comment.*?\(([0-9]*)', content)
    WB_forward = re.findall(r'WB\_text[^>]*>.*?fl_forward.*?>.*?\(([0-9]*)', content)
    WB_mid = re.findall(r' mid=\\"([0-9]*)', content)
    # print it
    return WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid


def showweibo(WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward,
        WB_mid):
    for i in range(0, len(WB_text)):
        print str(i + 1) + '.' + WB_text[i].lstrip('\\n').strip()
        print 'time:' + WB_time[i]
        print 'mid:' + WB_mid[i]
        print 'comefrom:' + WB_comefrom[i]
        print 'like:' + WB_like[i]
        print 'forward:' + WB_forward[i]
        print 'pinlun:' + WB_pinlun[i]


def main():
    content = open('index.html').read()
    WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid = detail(content)
    showweibo(WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid)

if __name__ == '__main__':
    main()

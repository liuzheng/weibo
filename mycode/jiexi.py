#!/usr/bin/env python
# coding: utf-8
# Copyright(c) 2013
# Gmail:liuzheng712
#

import re
import string


def detail(content):
    tmp = re.findall(r'WB\_media\_expand SW\_fun2 S\_line1 S\_bg1\\">.*?nofollow', content)
    for tmp_r in tmp:
        content = content.replace(tmp_r, 's')
    # get all things
    WB_single = re.findall(r"tbinfo.*?>\\t\\t\\t", content)
    WB_text = ['a'] * len(WB_single)
    WB_time = ['a'] * len(WB_single)
    WB_comefrom = ['a'] * len(WB_single)
    WB_like = ['a'] * len(WB_single)
    WB_pinlun = ['a'] * len(WB_single)
    WB_forward = ['a'] * len(WB_single)
    WB_mid = ['a'] * len(WB_single)
    for i in range(0,len(WB_single)):
        WB_text[i] = ''.join(re.findall(r"WB\_text[^>]*>(.*?)<\\/div",
            WB_single[i])).lstrip('\\n').strip()
        WB_time[i] = ''.join(re.findall(r'WB\_text[^>]*>.*?date=\\"([0-9]*)',
            WB_single[i]))
        WB_comefrom[i] = ''.join(re.findall(r'WB\_text[^>]*>.*?nofollow\\">(.*?)<',
            WB_single[i]))
        WB_like[i] = ''.join(re.findall(r'WB\_text[^>]*>.*?praised.*?\(([0-9]*)',
            WB_single[i]))
        WB_pinlun[i] = ''.join(re.findall(r'WB\_text[^>]*>.*?fl_comment.*?\(([0-9]*)',
            WB_single[i]))
        WB_forward[i] = ''.join(re.findall(r'WB\_text[^>]*>.*?fl_forward.*?>.*?\(([0-9]*)', 
            WB_single[i]))
        WB_mid[i] = ''.join(re.findall(r' mid=\\"([0-9]*)', WB_single[i]))
    return WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid


def showweibo(WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward,
        WB_mid):
    for i in range(0, len(WB_text)):
        print str(i + 1) + '.' + WB_text[i]
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

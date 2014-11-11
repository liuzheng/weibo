#!/usr/bin/env python
# coding: utf-8
# Copyright(c) 2013
# Gmail:liuzheng712
#

import re
import string


def detail(content):
    tmp = re.findall(r'pl\.content\.homeFeed\.index.*html\":\"(.*)\"}\)', content)
    # for tmp_r in tmp:
    #     content = content.replace(tmp_r, 's')
    max = 0
    for i in tmp:
        if max < len(i):
            max = len(i)
            content = i
    content = content.replace('WB_detail', 'WB_detailWB_detail')
    # get all things
    WB_single = re.findall(r"WB\_detail(.+?)WB\_detail", content)
    # for i in range(0,len(WB_single)):
    # {'text': 微博信息内容, 'count': 转发数, 'wid': 微博ID, 'name': 微博作者的用户信息字段, 'uid': 用户UID,
    #  'nick': 用户昵称, 'self': u['self'], 'timestamp': 微博创建时间, 'source': 微博来源,
    #  'location': 用户所在地, 'country_code': u['country_code'],
    #  'province_code': 用户所在省级ID, 'city_code': 用户所在城市ID, 'geo': 地理信息字段,
    #  'emotionurl': u['emotionurl'], 'emotiontype': u['emotiontype']
    # })
    # {'text': u['text'], 'count': u['reposts_count'], 'wid': u['id'], 'name': u['user']['name'],
    #  'uid': u['user']['id'],
    #  'nick': u['user']['screen_name'], 'self': 'null', 'timestamp': u['created_at'], 'source': u['source'],
    #  'location': u['user']['location'], 'country_code': '',
    #  'province_code': u['user']['province'], 'city_code': u['user']['city'], 'geo': u['geo'],
    #  # 'emotionurl': u['emotionurl'], 'emotiontype': u['emotiontype']
    #  'link': u['user']['id']
    # })
    user = []
    for WB in WB_single:
        WB_text = ''.join(re.findall(r"WB\_text[^>]*>(.*?)<\\/div", WB)).lstrip('\\n').strip()
        # WB_time = ''.join(re.findall(r'WB\_text[^>]*>.*?date=\\"([0-9]*)', WB))
        WB_source = ''.join(re.findall(r'WB\_text[^>]*>.*?nofollow\\">(.*?)<', WB))
        WB_forward = ''.join(re.findall(r'收藏 (\d*)', WB))
        WB_pinlun = ''.join(re.findall(r'评论 (\d*)', WB))
        WB_count = ''.join(re.findall(r'转发 (\d*)', WB))
        WB_like = ''.join(re.findall(r'WB\_text[^>]*>.*?praised.*?\(([0-9]*)', WB))
        # WB_mid = ''.join(re.findall(r' mid=\\"([0-9]*)', WB))
        WB_wid = ''.join(re.findall(r'mid=(\d*).*转发', WB))
        WB_name = ''.join(re.findall(r'nick-name=\\"([^"]*)\\"', WB))
        WB_uid = ''.join(re.findall(r'fuid=([^"]*)\\"', WB))
        WB_timestamp = ''.join(re.findall(r'date=\\"([^"]*)\\"', WB))
        user.append({'text': WB_text, 'count': WB_count,'wid':WB_wid,'name':WB_name,
                     'uid':WB_uid,'nick':WB_name,'self':'dontknow','timestamp':WB_timestamp,'source':WB_source,
                     'location':'null','country_code': '','province_code': 'null', 'city_code': 'null', 'geo': 'null',
                     'link': WB_uid,'forward':WB_forward,'like':WB_like,'pinlun':WB_pinlun})
    # for i in user:
    #     print i['name']
    # print len(user)
    return user #WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid


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
    content = open('/tmp/kaifu.html').read()
    print detail(content)
    # WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid = detail(content)
    # showweibo(WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid)


if __name__ == '__main__':
    main()

    # from pyquery import PyQuery as pq
    # from lxml import etree
    # d = pq(filename='/tmp/kaifu.html')
    # print d('.WB_feed')
    # content = open('/tmp/kaifu.html').read()
    # tmp = re.findall(r'pl\.content\.homeFeed\.index.*html\":\"(.*)\"}\)', content)
    # print tmp[0]
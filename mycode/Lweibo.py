#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#
__author__ = 'liuzheng'

import os
import sys
import re
from weiboAPI import Client
import ConfigParser
import webbrowser
from weibo_login import weibo_login

try:
    import cPickle as pkl
except:
    import pickle as pkl


class useAPI(object):
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'config.ini').replace('\\', '/'))
        APP_KEY = config.get('APPKEY', 'APP_KEY')
        APP_SECRET = config.get('APPKEY', 'APP_SECRET')
        CALLBACK_URL = config.get('APPKEY', 'CALLBACK_URL')
        token_file = os.path.join(os.path.dirname(__file__), 'token.pkl').replace('\\', '/')
        if os.path.isfile(token_file):
            try:
                token = pkl.load(open(token_file, 'r'))
                api = Client(APP_KEY, APP_SECRET, CALLBACK_URL, token)
                try:
                    api.get('statuses/user_timeline')
                    self.api = api
                    return
                except:
                    print "token maybe out of time!"
            except:
                print "The token file error"
        client = Client(APP_KEY, APP_SECRET, CALLBACK_URL)
        url = client.authorize_url
        webbrowser.open_new(url)
        CODE = raw_input("Please Input the Code: ").strip()
        try:
            client.set_code(CODE)
        except:
            print "Maybe wrong CODE"
            return
        token = client.token
        pkl.dump(token, file('token.pkl', 'w'))
        self.api = Client(APP_KEY, APP_SECRET, CALLBACK_URL, token)

    def get(self, url):
        return self.api.get(url)

    def post(self, url):
        return self.api.post(url)


class simu(object):
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), 'config.ini').replace('\\', '/'))
        username = config.get('simu', 'username')
        pwd = config.get('simu', 'pwd')
        # cookie_file = '/tmp/weibo_login_cookies.dat'
        self.simu = weibo_login(username, pwd)

    def detail(self, url):
        content = self.simu.getHTML(url)
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
            WB_text = ''.join(re.findall(r"WB\_text[^>]*>(.*?)<\\/div", WB)).replace('\\n','').replace('\\"','"').replace('\\/','/').strip()#.lstrip('\\n').strip()
            # if WB_text inclued WB_media_expand is miniPage !!!!!!
            WB_source = ''.join(re.findall(r'WB\_text[^>]*>.*nofollow\\">(.*?)<', WB)) # checked
            WB_forward = re.findall(r'收藏.*?(\d+)', WB)[-1] # checked
            WB_pinlun = re.findall(r'评论.*?(\d+)', WB)[-1] # checked
            WB_count = re.findall(r'转发.*?(\d+)', WB)[-1] # checked
            WB_like = ''.join(re.findall(r'WB\_text[^>]*>.*praised.*?\(([0-9]*)', WB))# checked
            # WB_mid = ''.join(re.findall(r' mid=\\"([0-9]*)', WB))
            WB_wid = re.findall(r'mid=(\d*).*?转发', WB)[-1] # checked
            WB_name = ''.join(re.findall(r'nick-name=\\"([^"]*)\\"', WB))
            WB_uid = ''.join(re.findall(r'fuid=([^"]*)\\"', WB)) # checked
            WB_timestamp = re.findall(r'date=\\"([^"]*)\\"', WB)[-1] # checked
            user.append({'text': WB_text, 'count': WB_count,'wid':WB_wid,'name':WB_name,
                         'uid':WB_uid,'nick':WB_name,'self':'dontknow','timestamp':WB_timestamp,'source':WB_source,
                         'location':'null','country_code': '','province_code': 'null', 'city_code': 'null', 'geo': 'null',
                         'link': WB_uid,'forward':WB_forward,'like':WB_like,'pinlun':WB_pinlun})
        # for i in user:
        #     print i['name']
        # print len(user)
        return user #WB_text, WB_time, WB_comefrom, WB_like, WB_pinlun, WB_forward, WB_mid


if __name__ == '__main__':
    # api = useAPI()
    # print api.get('statuses/user_timeline')
    # config = ConfigParser.ConfigParser()
    # config.read(os.path.join(os.path.dirname(__file__), 'config.ini').replace('\\', '/'))
    # username = config.get('simu', 'username')
    # pwd = config.get('simu', 'pwd')
    # html = weibo_login(username, pwd)
    # print html.getHTML('http://www.weibo.com/kaifulee')
    aa = simu()
    print aa.detail('http://weibo.com/kaifulee')
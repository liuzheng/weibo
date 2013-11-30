#!/usr/bin/env python2
#coding=utf8
import urllib
import urllib2
import cookielib
import base64
import re
import json
import hashlib
import rsa
import binascii

# get a cookie object to save
cj = cookielib.LWPCookieJar()
# make this cookie object and a http-cookie-processor binding
cookie_support = urllib2.HTTPCookieProcessor(cj)
# make a opener which will save http-cookie-processor,and make a handler to open the URL
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
# combine all this
urllib2.install_opener(opener)

postdata = {
    'entry': 'weibo',
    'gateway': '1',
    'from': '',
    'savestate': '7',
    'userticket': '1',
    'pagerefer': '',
#    'ssosimplelogin': '1',
    'vsnf': '1',
#    'vsnval': '',
    'su': '',
    'service': 'miniblog',
    'servertime': '',
    'nonce': '',
    'pwencode': 'rsa2',
    'rsakv': '',
    'sp': '',
    'encoding': 'UTF-8',
    'prelt': '',
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    'returntype': 'META'
}


def main():
    username = ''  # your account
    password = ''  # password you need type in
    url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)'
    #url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1384076174'
    # the last & seems not important
    data = urllib2.urlopen('http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)').read()
    p = re.compile('\((.*)\)')
    json_data = p.search(data).group(1)
    data = json.loads(json_data)
    servertime = str(data['servertime'])
    nonce = data['nonce']
    pubkey = data['pubkey']
    rsakv = data['rsakv']

    global postdata
    print postdata
    postdata['servertime'] = servertime
    postdata['nonce'] = nonce

    # calc su
    postdata['su'] = base64.b64encode(urllib.quote(username))

    # calc sp
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537)
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    sp = binascii.b2a_hex(rsa.encrypt(message, key))
    postdata['sp'] = sp

    postdata['rsakv'] = rsakv

    postdata = urllib.urlencode(postdata)
    print postdata
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.65 Safari/537.36'}
    #其实到了这里，已经能够使用urllib2请求新浪任何的内容了，这里已经登陆成功了
    req = urllib2.Request(url=url, data=postdata, headers=headers)
    result = urllib2.urlopen(req)
    text = result.read()
    p = re.compile('location\.replace\(\"(.*?)\"\)')
    try:
        login_url = p.search(text).group(1)
        #print login_url
        urllib2.urlopen(login_url)
        print "login success"
    except:
        print 'Login error!'
#    #测试读取数据，下面的URL，可以换成任意的地址，都能把内容读取下来
    req = urllib2.Request(url='http://e.weibo.com/aj/mblog/mbloglist?page=1&count=15&max_id=3463810566724276&pre_page=1&end_id=3458270641877724&pagebar=1&_k=134138430655960&uid=2383944094&_t=0&__rnd=1341384513840',)
    result = urllib2.urlopen(req)
    text = result.read()
    print len(result.read())
    #unicode(eval(b), "utf-8")
    print eval("u'''" + text + "'''")
main()

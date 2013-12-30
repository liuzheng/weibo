#!/usr/bin/env python2
# coding:utf-8
# Gmail:liuzheng712

import sys
import requests
import base64
import re
import urllib
import rsa
import json
import binascii
import getpass
import persion
import file


def Login():
    # username = 'username'
    # password = 'password'
    username = raw_input("Input the UserName: ").strip()
    password = getpass.getpass("Input the PassWord: ")
    return username, password


def rePasswd():
    password = getpass.getpass("Input the PassWord: ")
    return password


def getAPI(session, API):
    json_data = session.get(API)
    return json_data.content


def getCookies(username, password):
    session = requests.Session()
    url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&\
            callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&\
            client=ssologin.js(v1.4.5)&_=1364875106625'
    url_login = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.5)'
    # get servertime,nonce, pubkey,rsakv
    resp = session.get(url_prelogin)
    json_data = re.search('\((.*)\)', resp.content).group(1)
    data = json.loads(json_data)
    servertime = data['servertime']
    nonce = data['nonce']
    pubkey = data['pubkey']
    rsakv = data['rsakv']
    # calculate su
    su = base64.b64encode(urllib.quote(username))
    # calculate sp
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537)
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    sp = binascii.b2a_hex(rsa.encrypt(message, key))
    # define postdata
    postdata = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'userticket': '1',
        'ssosimplelogin': '1',
        'vsnf': '1',
        'vsnval': '',
        'su': su,
        'service': 'miniblog',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'sp': sp,
        'encoding': 'UTF-8',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&\
                callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META',
        'rsakv': rsakv
        }
    resp = session.post(url_login, data=postdata)
    login_url = re.findall('replace\("(.*)"\)', resp.content)
    #print login_url
    resp = session.get(login_url[0])
    if len(re.findall(r'true', resp.content)) == 0:
        print 'login error!'
        return 0
    else:
        print 'login success!'
        return session


def PageOne(session):
    who = raw_input("Who U want to see:(url)").strip()
    url = who
    if len(re.findall(r'\/', url)) == 0:
        url = 'http://weibo.com/u/' + url
    elif len(re.findall(r':', who)) == 0:
        url = 'http://' + url
    who = re.findall(r".*\/(.*)", url)
    # your local page
    #uid = re.findall('"uniqueid":"(\d+)",', resp.content)[0]
    #url = "http://weibo.com/u/"+uid
    #resp = session.get(url)
    #print resp.content
    resp = session.get(url)
    #print resp.content
    # Save file to index.html
    #file = open('index.html', 'w')
    #file.write(resp.content)
    #file.close()
    newlink = re.findall(r'PRF\_feed\_list\_more.*?href=\\"(.*?)\\"', resp.content)
    while len(newlink) == 0:
        session = getCookies(persion.usename, persion.passwd)
        resp = session.get(url)
        newlink = re.findall(r'PRF\_feed\_list\_more.*?href=\\"(.*?)\\"', resp.content)
    newlink = newlink[0]
    tmp = re.findall(r'\\', newlink)
    for tmp_r in tmp:
        newlink = newlink.replace(tmp_r, '')
    newlink = 'http://weibo.com' + newlink
    resp = session.get(newlink)
    return resp.content, who


def getPage(session, url):
    resp = session.get(url)
    who = re.findall(r".*\/(.*)", url)
    newlink = re.findall(r'PRF\_feed\_list\_more.*?href=\\"(.*?)\\"', resp.content)
    while len(newlink) == 0:
        session = getCookies(persion.usename, persion.passwd)
        resp = session.get(url)
        print time.time(),':Failure!:',who
        #fuck = open('fuck','w')
        #fuck.write(resp.content)
        #fuck.close
        #hehe = raw_input()
        newlink = re.findall(r'PRF\_feed\_list\_more.*?href=\\"(.*?)\\"', resp.content)
    newlink = newlink[0]
    tmp = re.findall(r'\\', newlink)
    for tmp_r in tmp:
        newlink = newlink.replace(tmp_r, '')
    newlink = 'http://weibo.com' + newlink
    resp = session.get(newlink)
    return resp.content, who


def waitlist(session):
    SinaAPI = 'https://api.weibo.com/2/statuses/public_timeline.json'
    if len(persion.access_token) == 0:
        print "you don't have access_token? http://open.weibo.com/"
    else:
        text = getAPI(session, SinaAPI + '?' + persion.access_token)
        result = re.findall(r'{"id":([0-9]*)', text)
        for i in range(0, len(result)):
            file.inputlist('waitlist', result[i])


def main():
    username, password = Login()
    session = getCookies(username, password)
    if session == 0:
        password = rePasswd()
        session = getCookies(username, password)
    if session == 0:
        username, password = Login()
        session = getCookies(username, password)
    if session == 0:
        password = rePasswd()
        session = getCookies(username, password)
    if session == 0:
        print 'Sorry GoodBye~'
        sys.exit(0)
    content, who = PageOne(session)
    # Save file to index.html
    file = open('index.html', 'w')
    file.write(content)
    file.close()


def help():
    print "Login():username, password"
    print "getCookies(username, password):session"
    print "PageOne(session):weiboPageHTML, who"
    print "getPage(session, url):weiboShortPageHTML, who"

if __name__ == "__main__":
    main()

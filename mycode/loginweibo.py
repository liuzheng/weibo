#!/usr/bin/env python2
#coding:utf-8
import requests
import base64
import re
import urllib
import rsa
import json
import binascii
import getpass

# username = 'username'
# password = 'password'
username = raw_input("Input the UserName: ").strip()
password = getpass.getpass("Input the PassWord: ")

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
    'rsakv': rsakv,
    }
resp = session.post(url_login, data=postdata)
login_url = re.findall('replace\("(.*)"\)', resp.content)
#print login_url
resp = session.get(login_url[0])
#print resp.content

# your local page
uid = re.findall('"uniqueid":"(\d+)",',resp.content)[0]
url = "http://weibo.com/u/"+uid
resp = session.get(url)
print resp.content

url = "http://weibo.com/kaifulee"
resp = session.get(url)
print resp.content

# Save file to index.html
file = open('index.html', 'w')
file.write(resp.content)
file.close()

url ="http://weibo.com/p/1035051197161814/weibo?from=page_103505_home&wvr=5.1&mod=weibomore#3639593649753032"
resp = session.get(url)
file = open('index1.html','w')
file.write(resp.content)
file.close()

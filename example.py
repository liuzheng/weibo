#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#
__author__ = 'liuzheng'

import Lweibo

def apiExample():
    # API 参考 http://open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI
    # 使用参考 https://github.com/lxyu/weibo
    api = Lweibo.useAPI()
    print api.get('statuses/user_timeline')
    print api.post('statuses/update', status='test from my api')

def simuLogin():
    # 模拟登陆的功能扩展待完善
    simu = Lweibo.simu()
    print simu.detail('http://weibo.com/kaifulee')

if __name__ == '__main__':
    apiExample()

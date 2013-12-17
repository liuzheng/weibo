#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#

import sys
import os

Wpath = 'weibo'

def checkdir(path):
    if os.path.exists(path) == 0:
        os.mkdir(path)

def inputtxt(who, text, time, mid, comefrom, like, forward, pinlun):
    checkdir(Wpath + '/' + who[0])
    file = open(Wpath + '/' + who[0] + '/' + str(mid), 'w')
    for i in range(0,len(text)):
        file.write(text[i])
    file.write('\n')
    file.write(time)
    file.write('\n')
    file.write(comefrom)
    file.write('\n')
    file.write(like)
    file.write('\n')
    file.write(forward)
    file.write('\n')
    file.write(pinlun)
    file.close()


checkdir(Wpath)

if __name__ == '__main__':
    checkdir(Wpath)

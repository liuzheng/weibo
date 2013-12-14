#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#

import time


def task():
    print "task ..."


def timer(n):
    while True:
        print time.strftime('%Y-%m-%d %X', time.localtime())
        task()
        time.sleep(n)

if __name__ == '__main__':
    timer(5)

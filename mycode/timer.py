#!/usr/bin/env python
# coding: utf-8
# Copyright(c) 2013
# Gmail:liuzheng712
#

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)
print time.time
print time.sleep


def print_event(name):
    print 'EVENT:', time.time(), name

print 'START:', time.time()
for i in range(1, 86400):
    scheduler.enter(i, 1, print_event, ('first' + str(i),))

scheduler.run()

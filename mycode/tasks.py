#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#


from celery.task import task

@task
def add(x, y):
    return x + y

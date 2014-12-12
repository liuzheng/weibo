#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2013
# Gmail:liuzheng712
#

import sys
import os
sys.path.insert(0, os.getcwd())

CELERY_IMPORTS = ("tasks", )

CELERY_RESULT_BACKEND = "amqp"

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"

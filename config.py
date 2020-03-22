#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wangjifei"
# @file: config.py
# Date: 2020/3/22

import os

BASE_DIR = os.path.dirname(__file__)

# 参数
options = {
    'port': 8000
}

# 配置web.Application
settings = {
    'static_path': os.path.join(BASE_DIR, 'static'),
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'debug': True
}

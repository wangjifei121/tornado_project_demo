#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wangjifei"
# @file: server.py
# Date: 2020/3/22

import tornado.ioloop
import tornado.web
import config
from application import Application

if __name__ == "__main__":
    app = Application()
    app.listen(config.options['port'])
    tornado.ioloop.IOLoop.current().start()

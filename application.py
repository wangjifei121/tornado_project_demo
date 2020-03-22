#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wangjifei"
# @file: application.py
# Date: 2020/3/22

import tornado.web
from views import views
import config


class Application(tornado.web.Application):
    """url 类"""

    def __init__(self):
        handlers = [
            (r"/", views.MainHandler),
        ]
        super(Application, self).__init__(handlers, **config.settings)

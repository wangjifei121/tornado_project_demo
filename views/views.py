#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wangjifei"
# @file: views.py
# Date: 2020/3/22
from tornado.web import RequestHandler


class MainHandler(RequestHandler):

    def get(self):
        self.write("Hello, world")

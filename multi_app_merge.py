#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'multi_app_merge'
__author__ = 'JieYuan'
__mtime__ = '2019-05-01'
"""
from myweb.app import app as myapp

from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask

app = Flask(__name__)
app.secret_key = 'topLevel'


@app.route('/')
def index():
    return 'Hello top level!'


app = DispatcherMiddleware(app, {
    '/app1': myapp,
    '/app2': myapp
})

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, app, use_reloader=True, use_debugger=True, use_evalex=True)

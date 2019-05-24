#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'app'
__author__ = 'JieYuan'
__mtime__ = '2019-04-30'
"""
import pandas as pd
from pytz import timezone
from flask import Flask, request, render_template, jsonify, redirect, url_for

import json

app = Flask(__name__)

dic = {}
tz = timezone('Asia/Shanghai')
# icon = 'https://static.easyicon.net/preview/119/1193422.gif'
# img = 'https://cloud.d.xiaomi.net/react/static/media/LOGO36.d3d970c2.png'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/meeting', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/meeting', methods=['POST'])
def signin():
    _ = request.form
    name, project, progress = _['name'], _['project'], _['progress']
    text = "{}@{}: \n{}".format(project, name, progress)

    ################################################################
    # 清空前一天数据，只保留当天数据
    date = pd.datetime.now(tz).date()
    for k in dic.keys():
        if k < str(date):
            dic.pop(k)

    dic.setdefault(str(date), {})[name] = text
    # from pprint import pprint
    # pprint (dic)
    ################################################################

    # 重定向
    # return redirect('meeting_result')  # redirect('路由') 路由：redirect(url_for('路由函数'))
    return render_template('form.html', text=text, dic=dic)


@app.route('/meeting_result', methods=['GET'])
def meeting_result():
    return jsonify(dic)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Hello
   Description :   Flask hello
   Author :        Liangz
   date：          2018/8/4
-------------------------------------------------
   Change Activity:
                   2018/8/4:
-------------------------------------------------
"""
__author__ = 'Liangz'

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
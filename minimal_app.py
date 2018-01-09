# -*- coding:utf-8 -*-
"""
最基本的应用
"""

from flask import Flask


app = Flask(__name__)


# 根目录的访问
@app.route("/")
def index():
    return "<b>Hello World</b>"


# 带参数的访问
@app.route("/user/<name>")
def name(name):
    return "<b>Hello %s</b>" % name


if __name__ == '__main__':
    app.run(debug=True)

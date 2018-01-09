# -*- coding:utf-8 -*-
"""
使用script manager 管理app
"""

from flask import Flask
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)

# 根目录的访问
@app.route("/")
def index():
    return "<b>Hello World</b>"




if __name__ == '__main__':
    manager.run()

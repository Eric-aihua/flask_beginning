# -*- coding:utf-8 -*-
from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
# 初始化 Flask-Bootstrap 之后，就可以在程序中使用一个包含所有 Bootstrap 文件的基模板。

bootstrap = Bootstrap(app)

# bootstrap 页面
@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap_user.html' , name='Eric')

if __name__ == '__main__':
    app.run()
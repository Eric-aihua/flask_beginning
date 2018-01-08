# -*- coding:utf-8 -*-
from flask import Flask,render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user=name)

# 引用macros的页面
@app.route('/jinja')
def jinja():
    comments = range(10)
    return render_template('controller.html', comments=comments)

# template继承
@app.route('/sub')
def sub():
    return render_template('sub.html')



if __name__ == '__main__':
    app.run(debug=True)
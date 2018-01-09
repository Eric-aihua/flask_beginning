# -*- coding:utf-8 -*-
from flask import Flask, render_template, redirect,url_for,session,flash
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'stronger key'
moment = Moment(app)
bootstrap = Bootstrap(app)

"""
Login form
"""


class LoginForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    pwd = PasswordField('What is your pwd?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    form = LoginForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            # 通过flash函数，可以将消息放入队列中供前段消费，该队列的数据只会被前段展示一次
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        # 使用post重定向到get的方式，来避免因为刷新页面而提示需要再次提交的警告。
        # 尽量不要让POST作为浏览器发送的最后一个请求
        return redirect(url_for('login_form'))

    return render_template('login.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    app.run()

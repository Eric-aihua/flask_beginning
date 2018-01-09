# -*- coding:utf-8 -*-
import os
from flask import Flask, render_template, redirect, url_for, session, flash
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Shell, Manager
from flask.ext.migrate import Migrate, MigrateCommand
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'stronger key'
moment = Moment(app)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

# 在启动shell的时候，将app,db,User,Role自动import，而不需要再收到执行from ... import
manager.add_command("shell", Shell(make_context=make_shell_context))

"""
Login form
"""


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


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
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['know'] = False
        else:
            session['know'] = True
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
    manager.run()

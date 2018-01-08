# -*- coding:utf-8 -*-
from flask import Flask,render_template
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from datetime import datetime
app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)


# bootstrap 页面
@app.route('/')
def index():
    return render_template('time_stamp.html',
                           current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run()
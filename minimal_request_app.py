# -*- coding:utf-8 -*-
"""
最基本的应用,通过request对象获取请求信息
"""

from flask import make_response,redirect,request,Flask


app = Flask(__name__)

# 根目录的访问
@app.route("/")
def index():
    return "<b>Hello World</b>\nBrowser is %s" %(request.headers.get('User-Agent'))


# 自定义状态码
@app.route("/notallow")
def not_allow():
    return "<b>Not be allowed</b>",500

# 指定response对象
@app.route("/response")
def resp():
    response=make_response("this reponse contain a cookie!",300)
    response.set_cookie("answer",'42')
    return response

# 指定response对象
@app.route("/redict")
def redirect_tobaidu():
    return redirect("http://www.baidu.com")

if __name__ == '__main__':
    app.run(debug=True)

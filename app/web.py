# coding:utf-8

from flask import Flask,url_for,request,render_template,Response
import database
import json
import httputil
import threading
import time



app = Flask(__name__)

@app.route('/lcfindex')
def index():
    return render_template('index.html')

@app.route('/lcfpack')
def pack():
    return render_template('package.html')

@app.route('/lcfauto')
def lcfauto():
    return render_template('auto.html')

@app.route('/lcfinter')
def lcfinter():
    return render_template('interface.html')



@app.route('/packaction')
def pac():
    httputil.checkupdat("debug")
    a = database.select()
    return json.dumps(a)

@app.route('/jenkins')
def jenkins():
    if httputil.request('debug') == "loading":
        return "loading"
    return ""

with app.test_request_context():
    print url_for('index')


if __name__ == "__main__":
    app.run(debug=True)

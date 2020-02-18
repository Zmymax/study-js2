from flask import Flask, url_for, request
import requests
from flask_cors import *  # 导入模块

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域


@app.route('/weather/api')
def hello_world():
    location = request.args.get("location")
    r=requests.get('https://api.seniverse.com/v3/weather/daily.json?key=SOXVOUP0VMWVEY77h&location='+location+'&language=zh-Hans&unit=c&start=0&days=15')
    return r.text

@app.route('/common/api')
def commonApi():
    url = request.args.get("url")
    r=requests.get(url)
    return r.text

@app.route('/ticket/api')
def ticketApi():
    url = request.args.get("url")
    r=requests.get(url)
    return r.text

app.run()

url_for('static', filename='4.html')

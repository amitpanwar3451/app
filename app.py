from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
import json
import urllib.request, urllib.error, urllib.parse
import requests
import pprint
from env import *
from routes import *
app.register_blueprint(routes)
@app.route('/')
def get():
    try:
        import urllib.request
        with urllib.request.urlopen(dynamodburl) as dynamodb:
            dynamodbdata = dynamodb.read()
    except:
        dynamodbdata = 'Not Found'
    try:
        import urllib.request
        with urllib.request.urlopen(dynamodburl) as rds :
            rdsdata = rds.read()
    except:
        rdsdata = 'Not Found'
    return render_template('index.html',dynomodbstatus = dynamodbdata ,rdsstatus = rdsdata)

@app.route('/',methods = ['GET','POST'])
def post():
   if request.method == 'POST':
       if request.form['submit'] == 'submit':
            email = request.form['test']
            return render_template('index.html',data2 = email)







if __name__ == '__main__':
    app.run(port = 8000)
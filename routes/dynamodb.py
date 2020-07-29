
from flask import Flask, render_template, request, url_for, redirect
import json
import urllib.request, urllib.error, urllib.parse
import requests
import pprint
from env import *
from . import routes


@routes.route('/dynomodb')
def dynomo():
      return render_template("dynomodb.html")

@routes.route('/dynomodb',methods = ['GET','POST'])
def post2():
   if request.method == 'POST':
       if request.form['submit2'] == 'submit2':
            try:
                  email = request.form['email']
                  name = request.form['name']
                  phone = request.form['phone']
                  r = requests.post(f"{dynamodburl}?name={name}&email={email}&phone={phone}")
                  return render_template('dynomodb.html',data2 = 'SuccessFully Added')
            except:
                  return render_template('dynomodb.html',data2 = 'Something Went Wrong!!!!')
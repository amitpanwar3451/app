from flask import Flask, render_template, request, url_for, redirect
import json
import urllib.request, urllib.error, urllib.parse
import requests
import pprint
from env import *
from . import routes
from pymongo import MongoClient

@routes.route('/mongodb')
def mongo():
      return render_template("mongodb.html")

@routes.route('/mongodb',methods = ['GET','POST'])
def mongo2():

      client = MongoClient(mongourl,serverSelectionTimeoutMS = 2000)
      db = client.pymongo_test
      db = client[DBNAME]
      posts = db[COLLECTIONNAME]
      email = request.form['email']
      name = request.form['name']
      phone = request.form['phone']
      if request.method == 'POST':
            if request.form['submit'] == 'submit2':
                  result = posts.insert_one({'NAME': name,'EMAIL': email,'PHONE': phone})
                  return render_template('mongodb.html', data3 = 'SUCCESSFULLY ADDED' )
            elif request.form['submit'] == 'get_by_name':
                  y = posts.find_one({'NAME': name})
                  return render_template('mongodb.html', data3 = y )
            elif request.form['submit'] == 'check':
                  try:
                        client.server_info()
                        return render_template('mongodb.html', data3 = 'Connected' )
                  except:
                        return render_template('mongodb.html', data3 = 'SOMETHING WRONG' )




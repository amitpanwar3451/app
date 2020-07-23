
from flask import render_template
from . import routes


@routes.route('/dynomodb')
def dynomo():
      return render_template("dynomodb.html")

@routes.route('/dynomodb',methods = ['GET','POST'])
def post2():
   if request.method == 'POST':
       if request.form['submit2'] == 'submit2':
             email = request.form['email']
             name = request.form['name']
             phone = request.form['phone']
             r = requests.post(f"{dynamodburl}?name={name}&email={email}&phone={phone}")
             import urllib.request
             with urllib.request.urlopen(dynamodburl) as response:
               html = response.read()
             
             return render_template('dynomodb.html',data2 = html)
# from flask import render_template
# from . import routes
# from env import *
# import psycopg2
# connection = psycopg2.connect(
#     host = RDSHOST,
#     port = RDSPORT,
#     user = RDSUSER,
#     password = RDSPASS,
#     database= RDSDBNAME
# )


# @routes.route('/rds')
# def rds():
#     return render_template("rds.html")

# @routes.route('/rds',methods = ['GET','POST'])
# def rdspost():
#     if request.method == 'POST':
#        if request.form['check'] == 'Check-Database':
#             return render_template('rds.html',data2 = cursor)
#        if request.form['create'] == 'Create-Schema':
#              return render_template('rds.html',data2 = table)
#        if request.form['submit'] == 'submit':
#              email2 = request.form['email']
#              name2 = request.form['name']
#              phone2 = request.form['phone']    
#              return render_template('rds.html',data2 = 'Data Successfully Inserted')
#        if request.form['get'] == 'get-value':
#              return render_template('rds.html',data2 = data)       


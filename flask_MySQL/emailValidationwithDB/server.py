from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitemail', methods=['POST'])
def create():
    if len(request.form['email']) < 1:
        flash("Email is not valid!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
        return redirect('/')
    else:
        flash("The email address you entered {} is a VALID email address! Thank you! ".format(request.form['email']))
        query = "INSERT INTO email_validation_table (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
                 'email': request.form['email']
               }
        mysql.query_db(query, data)
        return redirect('/taco')

@app.route('/taco')
def select():
    query = "SELECT  * FROM email_validation_table"
    friends = mysql.query_db(query)
    return render_template('success.html', all_friends=friends)

app.run(debug=True)

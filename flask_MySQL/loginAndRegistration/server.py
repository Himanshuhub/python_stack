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

@app.route('/submitregistration', methods=['POST'])
def create():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']

    flash("The data you entered {} is as follows! Thank you! ".format(email))
    query = "INSERT INTO registration (firstname, lastname, email, password, created_at, updated_at) VALUES (:firstname, :lastname, :email, :password, NOW(), NOW())"
    data = {'firstname':firstname, 'lastname':lastname, 'email':email, 'password':password }
    registrants = mysql.query_db(query, data)
    return redirect('/taco')

# submitlogin
@app.route('/submitlogin', methods=['POST'])
def loginmethod():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT email, password from registration where email = :email and password=:password"
    data = {'email':email, 'password':password }
    login_registrants = mysql.query_db(query, data)
    if login_registrants:
        flash("Successful Login!")
    else:
        flash("unsuccessfull Login! ")
    return redirect('/taco')


@app.route('/taco')
def select():
    query = "SELECT  * FROM registration"
    registrants = mysql.query_db(query)
    print "taco"
    return render_template('success.html', all_registrants=registrants)

app.run(debug=True)

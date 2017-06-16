from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
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


    if len(email) < 1:
        flash("Email is not valid!")
    elif not EMAIL_REGEX.match(email):
        flash("Email is not valid!")

    elif len(firstname) < 3:
        flash("Please enter more than 2 characters in First Name!")
    elif not firstname.isalpha():
        flash("Please enter only characters in First Name!")

    elif len(lastname) < 3:
        flash("Please enter more than 2 characters in Last Name!")
    elif not lastname.isalpha():
        flash("Please enter only characters in Last Name!")

    elif len(password) < 9:
        flash("Please enter more than 8 characters in Password!")

    else:
        query = "SELECT email from registration where email = :email"
        data = {'email': email}
        duplicateemail = mysql.query_db(query, data)
        if duplicateemail:
            flash("Email is already registered!")
        else:
            flash("The Registration details are {} {} {} {}! Thank you! ".format(firstname, lastname, email, password))
            query = "INSERT INTO registration (firstname, lastname, email, password, created_at, updated_at) VALUES (:firstname, :lastname, :email, :password, NOW(), NOW())"
            hashed_password = md5.new(password).hexdigest()
            data = {'firstname':firstname, 'lastname':lastname, 'email':email, 'password':hashed_password }
            registrants = mysql.query_db(query, data)


    return redirect('/taco')

# submitlogin
@app.route('/submitlogin', methods=['POST'])
def loginmethod():
    email = request.form['email']
    password = request.form['password']
    hashed_password = md5.new(password).hexdigest()
    query = "SELECT email, password from registration where email = :email and password=:password"
    data = {'email':email, 'password':hashed_password }
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

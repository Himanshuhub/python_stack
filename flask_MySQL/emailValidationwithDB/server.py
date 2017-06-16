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

@app.route('/taco')
def select():
    query = "SELECT  * FROM email_validation_table"
    emailFromQuery = mysql.query_db(query)
    return render_template('success.html', all_emailFromQuery=emailFromQuery)



@app.route('/submitemail', methods=['POST'])
def create():
    email = request.form["email"].lower()

    if len(email) < 1:
        flash("Email is not valid!")
    elif not EMAIL_REGEX.match(email):
        flash("Email is not valid!")
    else:
        query = "SELECT email from email_validation_table where email = :email"
        data = {'email': email}
        duplicateemail = mysql.query_db(query, data)
        if duplicateemail:
            flash("Email is already entered!")
        else:
            flash("The email address you entered {} is a VALID email address! Thank you! ".format(email))
            query = "INSERT INTO email_validation_table (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
            mysql.query_db(query, data)
            return redirect('/taco')

    return redirect('/')
app.run(debug=True)

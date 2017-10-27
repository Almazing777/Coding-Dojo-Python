from flask import Flask, request, redirect, render_template, session, flash

from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])')

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_db')
app.secret_key = "secretkey"


@app.route('/')
def index():
	    return render_template('index.html')

@app.route('/registration', methods=["POST"])
def registration():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['pwd']
    confirm = request.form['pwd_confirm']
    errors = False

    if first_name == "" or len(first_name) <2:
        flash('First Name must be atleast 2 characters long')
        errors = True
    
    if last_name == "" or len(last_name) <2:
        flash('Last Name must be atleast 2 characters long')
        errors = True

    if not EMAIL_REGEX.match(email):
        flash('Email is not valid')
        errors = True
       
    if password =='':
        flash('password cannot be empty')
        errors = True

    if confirm != password:
        flash('passwords must match')
        errors = True

    if not errors:
        flash('Successful Registration! Login using your email')
        query = "INSERT INTO users(`first_name`, `last_name`, `email`, `password`) VALUES(:first_name, :last_name, :email, :password);"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': request.form['pwd']
        }
        mysql.query_db(query, data)
        return redirect('/')


@app.route('/login', methods = ["POST"])
def login():
    email = request.form["email"]
    password = request.form["pwd"]
    query = "SELECT * FROM users WHERE email=:email"
    data = {
        "email": email
    }
    user = mysql.query_db(query, data)

    if len(user) == 0:
        flash ('not real user name')
        return redirect ('/')
    else:
        user = user[0]
        if user["password"] == password:
            flash("logged in")
            return render_template('success.html')
            session["id"] = user.id
        else:
            flash("invalid password")
            return redirect ('/')


@app.route('/logout')
def logout():
    return render_template('index.html')


app.run(debug=True)
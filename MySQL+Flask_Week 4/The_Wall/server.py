from flask import Flask, request, redirect, render_template, session, flash
from datetime import datetime
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD_REGEX = re.compile(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])')

app = Flask(__name__)
mysql = MySQLConnector(app,'wall_db')
bcrypt = Bcrypt(app)
app.secret_key = "secretkey"


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/registration', methods=["POST"])
def registration():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['password_confirm']
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
        return redirect('/')

    if not errors:
        flash('Successful Registration! Login using your email')

        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)

        query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'pw_hash': pw_hash
        }
        mysql.query_db(query, data)
      
    return redirect('/')


@app.route('/login', methods = ["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    query = "SELECT * FROM users WHERE email=:email LIMIT 1"
    data = {"email": email}
    user = mysql.query_db(query, data)

    if not user:
       flash("Please enter valid email")
       return redirect ('/')

    elif bcrypt.check_password_hash(user[0]['password'], password):
        session['user_id'] = user[0]['id']
        return redirect('/wall')
    else:
        flash('Invalid login!')
        return redirect ('/')


@app.route('/logout')
def logout():
    return redirect ('/')


@app.route('/wall')
def wall():
    query = 'SELECT users.first_name, users.last_name, messages.message, messages.id, messages.created_at FROM messages JOIN users ON messages.user_id=users.id'
    comment_query = 'SELECT comments.user_id, comments.comment, comments.message_id, users.first_name, users.last_name FROM comments INNER JOIN users ON users.id=comments.user_id INNER JOIN messages ON messages.id = comments.message_id'
    messages = mysql.query_db(query)
    comments = mysql.query_db(comment_query)
    return render_template('wall.html', messages=messages, comments=comments)


@app.route('/message', methods = ["POST"])
def message():
    data = {
            'currentsession': session['user_id'],
            'user_message': request.form['add_message']
            }
    query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:currentsession, :user_message, NOW(), NOW())'
    mysql.query_db(query,data)
    return redirect('/wall')


@app.route('/addcomment/<id>', methods=['POST'])
def comment(id):
    data = {
        'specific_id': id,
        'currentsession': session['user_id'],
        'comment': request.form['addcommment']
    }
    
    query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at VALUES (:specific_id, :currentsession, :comment, NOW(), NOW())"
    comments = mysql.query_db(query, data)

    return redirect ('/wall')

app.run(debug=True)
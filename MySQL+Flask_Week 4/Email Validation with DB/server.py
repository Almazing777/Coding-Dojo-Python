from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key = "secretkey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods = ['POST'])
def process():
	email = request.form['email']
	errors = False

	if len(request.form['email']) == 0:
		flash('Email can not be empty')
		errors = True
		return redirect ('/')

	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Email is not valid')
		errors = True
		return redirect ('/')

	if not errors:
		flash('Successful Registration!')
		query = "INSERT INTO user_emails(email, created_at) VALUES(:email, NOW())"
		data = {
			'email': request.form['email']
			}
		session['email'] = email 
		mysql.query_db(query, data)
		return redirect('/success')
	

@app.route('/success')
def success():
	query = "SELECT * FROM user_emails"                           # define your query
	emails = mysql.query_db(query)                           # run query with query_db()
	return render_template('success.html', all_emails=emails, email=session['email'])

@app.route('/home')
def home():
	session.pop('email')
	return redirect('/')

@app.route('/remove/<id>')
def remove(id):
	query = "DELETE FROM user_emails WHERE id = :id"
	data = {'id': id}
	mysql.query_db(query,data)
	return redirect('/success')



app.run(debug=True)


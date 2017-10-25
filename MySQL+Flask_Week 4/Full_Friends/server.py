from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
app.secret_key = "secretkey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
 
    friends = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', all_friends = friends)


@app.route('/friends', methods = ['POST'])
def add_friend():
 	first_name = request.form['first_name']
 	last_name = request.form['last_name']
 	email = request.form['email']

	query = "INSERT INTO users(`first_name`,`last_name`,`email`) VALUES (:first_name, :last_name, :email)"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'], 
			'email': request.form['email']
			}
	mysql.query_db(query, data)
	return redirect('/')


@app.route('/friends/<id>/edit', methods = ["GET"])
def edit_friend(id):
	query = "SELECT * FROM users WHERE id=:id"
	data = {
			'id': id
	}
	friend = mysql.query_db(query, data)
	print friend
	return render_template('/edit.html', friend = friend)

@app.route('/friends/<id>', methods =["POST"])
def update_friend(id):
	query = "UPDATE users SET first_name= :first_name, last_name = :last_name, email =:email WHERE id = :id"
	data = {
			'id': id,
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email']
	}
	mysql.query_db(query, data)
	return redirect ('/')


@app.route('/friends/<id>/delete')
def remove(id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query,data)
    return redirect('/')


app.run(debug=True)
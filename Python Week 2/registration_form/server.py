from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
app.secret_key ="secretkey"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
	errors = False

	if len(request.form['email']) == 0:
		flash('email cannot be blank')
		errors = True

	if len(request.form['first']) == 0:
		flash('name cannot be blank')
		errors = True

	elif not request.form['first'].isalpha():
		flash('name cannot contain numbers')
		errors = True

	if len(request.form['last']) == 0:
		flash('last name cannot be blank')
		errors = True

	elif not request.form['last'].isalpha():
		flash('last name cannot contain numbers')
		errors = True

	if len(request.form['pwd']) < 8:
		flash('pwd cannot be more than 8 characters')
		errors = True

	elif len(request.form['pwd']) != request.form['confirm']:
		flash('pwds must match')
		errors = True

	if not errors: 
		flash('thanks for submitting your form!')
	
	return redirect('/')

app.run(debug=True)

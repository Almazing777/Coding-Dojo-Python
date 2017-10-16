from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
app.secret_key ="secretkey"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	if request.method == 'POST':
		if len(name) < 1:
			flash("Name is empty!")
			return render_template("index.html")
		elif len(comment) < 1:
			flash("Comment is empty!")
			return render_template("index.html")
		elif len(comment) > 120:
			flash("Comment cannot be longer than 120 characters!")
			return render_template("index.html")
		else:
			flash("Thank you".format(name))
			return render_template("results.html", name = name, location = location, language = language, comment = comment)
			return redirect('/result')

app.run(debug=True)

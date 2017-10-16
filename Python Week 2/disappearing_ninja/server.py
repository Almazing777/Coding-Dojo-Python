from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key ="secretkey"

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/ninja', methods=["POST"])
def show():
    turtles = [
        {'name': 'leonardo',
            'img': "/static/images/leonardo.jpg"},
        {'name': 'donatello',
            'img': "/static/images/donatello.jpg"},
        {'name': 'michelangelo',
            'img': "/static/images/michelangelo.jpg"},
        {'name': 'raphael',
            'img': "/static/images/raphael.jpg"}
    ]
    return render_template('results.html', turtles=turtles)





app.run(debug=True)

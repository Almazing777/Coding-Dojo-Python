from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/ninjas')
def info():
    return render_template("ninjas.html")

@app.route('/dojos')
def dojos():
    return render_template("dojos.html")

@app.route('/process', methods=["POST"])
def process():
    return "this is a new process route"


app.run(debug=True)

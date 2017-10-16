from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja', method='Post')
def show():
    print "/ninja"
    return render_template(results.html)

@app.route('ninja/<color>')
def color(color):
    print color

    if color.lower() == 'blue':
        ninja = "leonardo"
    elif color.lower() == 'orange':
        ninja = "michelangelo"
    elif color.lower() == 'red':
        ninja = 'raphael'
    elif color.lower() == 'purple':
        ninja = 'donatello'
    else:
        ninja = 'notapril'
    return render_template('results.html', ninja=ninja)




app.run(debug=True)
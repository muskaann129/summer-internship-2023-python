from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', data = {'name': 'Kunal'})

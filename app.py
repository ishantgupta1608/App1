from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save')
def save():
    return "Save"

@app.route('/hello')
def hello():
    return "Hello"

if __name__ == '__main__':
    #a
    app.run()

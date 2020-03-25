from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('hello')
def index():
    return "Hello"

if __name__ == '__main__':
    app.debug = True
    app.run()

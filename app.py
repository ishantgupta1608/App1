from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods = ['POST'])
def save():
    name = request.form['Name']
    number = request.form['Number']
    return name + ' : ' + str(number)

@app.route('/hello')
def hello():
    return "Hello"

if __name__ == '__main__':
    app.run()

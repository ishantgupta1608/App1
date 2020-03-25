from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sql:///test.db'
#db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods = ['POST'])
def save():
    name = request.form['Name']
    number = request.form['Number']
    #file = open(os.path.join("Data Files", name), 'a')
    #file.append(str(number) + '\n')
    return name + ' : ' + str(number)

@app.route('/hello') 
def hello():
    return app.root_path

if __name__ == '__main__':
    #print(os.path.join(app.instance_path, "Data Files", '1'))
    print(app.instance_path)
    app.run()

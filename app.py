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
    file = open(os.path.join(app.root_path, 'Data Files', name), 'a')
    file.write(str(number) + '\n')
    file.close()
    return name + ' : ' + open(os.path.join(app.root_path, 'Data Files', name), 'r').read()

@app.route('/hello') 
def hello(): 
    return str(os.listdir(app.root_path))

if __name__ == '__main__':
    #print(os.path.join(app.instance_path, "Data Files", '1'))
    print(app.instance_path)
    app.run()

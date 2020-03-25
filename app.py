from flask import Flask, render_template, request, send_file
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
    return str(os.listdir(os.path.join(app.root_path, 'Data Files')))

@app.route('/upload_file')
def upload_file():
    html = """
    <form action = "/upload_success" method = "post" enctype="multipart/form-data">
        <input type = "file" name = "file_name">
        <input type = "submit" name = "Upload">
    </form>
    """
    return html

@app.route('/upload_success', methods = ['POST'])
def upload_success():
    file = request.files['file_name']
    file.save(os.path.join(app.root_path, 'Uploads', file.filename))
    return file.filename + ' uploaded succesfully'
    #return str(os.listdir(os.path.join(app.root_path, 'Uploads')))

@app.route('/display_files')
def display_files():
    html = """
    <form action = "/download_file" method = "post">
        <input type = "text" name = "file_name">
        <input type = "submit" name = "Download">
    </form>
    
    """
    return html + str(os.listdir(os.path.join(app.root_path, 'Uploads')))

@app.route('/download_file', methods = ['POST'])
def download_file():
    return send_file(os.path.join(app.root_path, 'Uploads', 
                                  request.form['file_name']),  
                     as_attachment = True)
    
if __name__ == '__main__':
    #print(os.path.join(app.instance_path, "Data Files", '1'))
    print(app.instance_path)
    app.run()

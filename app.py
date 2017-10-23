# Code adapted from http://flask.pocoo.org/docs/0.12/quickstart/#
from flask import Flask
app = Flask(__name__)

'''
A template for how a route is defined. 
Routes need a annotation stating what route will call the function
Also needs a function name and some code to run when this route is accessed.
'''
@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/<path>')
def parrot_path(path):
    return 'You entered this path : '+ path
''' Commands to run the flask app : 

export FLASK_APP=hello.py

flask run
'''
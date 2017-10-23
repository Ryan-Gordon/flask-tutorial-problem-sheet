# Code adapted from http://flask.pocoo.org/docs/0.12/quickstart/#
from flask import Flask
import requests #Requests used to handle HTTP requests
import json #Requests used to handle json manipulation 
app = Flask(__name__)

'''
A template for how a route is defined. 
Routes need a annotation stating what route will call the function
Also needs a function name and some code to run when this route is accessed.
'''
@app.route('/')
def hello_world():
    return 'Hello, World!'


'''
Specifying a path as <path> allows you as the dev to take that part of the path as a variable
'''
@app.route('/<path>')
def parrot_path(path):
    return 'You entered this path : '+ path

'''
A practical example of a http request to an api, which will return data.
'''
@app.route('/http/<path>')
def http_example(path):
    # Pull JSON market data from Poloniex
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/'+path+'/')
    data = r.json() # Gather the json data
   
    return json.dumps(data)
    # end function


''' Commands to run the flask app : 

export FLASK_APP=hello.py

flask run
'''
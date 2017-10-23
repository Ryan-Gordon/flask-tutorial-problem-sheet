# Code adapted from http://flask.pocoo.org/docs/0.12/quickstart/#
from flask import Flask
import requests #Requests used to handle HTTP requests
import json #Requests used to handle json manipulation 
from api import api
from flask_cors import CORS
app = Flask(__name__) # Register the app itself
app.register_blueprint(api) # register a blueprint which is a separate fiel containing routes
CORS(app) # Set up some CORS 
''' 
Commands to run the flask app : 
export FLASK_APP=hello.py

flask run
'''

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
Please see api.py for more examples of a rest API 
'''
@app.route('/http/<path>')
def http_example(path):
    # Pull JSON market data from Poloniex
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/'+path+'/')
    data = r.json() # Gather the json data
    #Notice the lack of status code, we always return 200 here, unless internal error. NOT REST
    return json.dumps(data)

'''
Custom error handlers 
Used to handle any 404 or 500 and return a message rather than breaking the route 
'''
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500 



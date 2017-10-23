# -*- coding: utf-8 -*-
from flask import jsonify, Blueprint
import requests
api = Blueprint('api', __name__, url_prefix='/api/v1')

from decimal import Decimal
'''
A blueprint is one way to define a set of routes all under some common route such as api/v1 or api/v2
'''


'''
    API Calls included:
    - Top 100 results
    - All results
    - All results with local currency price
'''


# Api route to return 100 currencies from API.
@api.route('/top100')
def top100():
    req = requests.get('http://api.coinmarketcap.com/v1/ticker')
    json_data = req.json()[:100]
    return jsonify(data=json_data), 200


# Api route to return all currencies from API.
@api.route('/all')
def all():
    req = requests.get('http://api.coinmarketcap.com/v1/ticker')
    json_data = req.json()
    return jsonify(data=json_data), 200

# Api route to return currencies from api converted into a currency
# Currency must be entered in ticker format e.g EUR or GBP
# If not in this format will return default data to USD
@api.route('/all/<currency>')
def all_converted(currency):
    req = requests.get('http://api.coinmarketcap.com/v1/ticker/?convert='+currency.upper())
    json_data = req.json()[:100]
    return jsonify(data=json_data), 200


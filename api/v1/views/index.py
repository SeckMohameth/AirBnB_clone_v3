#!/usr/env/python
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify

@app_views.route('/status', methods=['GET'])
def status():
    '''status'''
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def st_count():

    '''retrieves the number of each objects by type'''
    cl_count = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(cl_count)

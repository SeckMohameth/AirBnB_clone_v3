#!/usr/env/python
from api.v1.views import app_views

@app_views.route('/status', method=['GET'])
def status():
    '''status'''
    return jsonify({"status": "OK"})

@app_views.route('/status')
def status():
    '''retrieves the number of each objects by type'''
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)

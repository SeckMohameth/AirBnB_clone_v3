#!/usr/env/python
from api.v1.views import app_views

@app_views.route('/status', method=['GET'])
def status():
    '''status'''
    return jsonify({"status": "OK"})

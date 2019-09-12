#!/usr/bin/python3
'''Flask App'''
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, make_response, jsonify, request
from os import getenv
from flask_cors import CORS

app = Flask(__name__, threaded=True)
app.register_blueprint(a--_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = TRUE

@app.teardown_appcontext
def tear_it_down(self):
    """Closes session"""
    storage.close()

@app.errorhandler(404)
def error_handler(error):
    """error handle 404"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    env_var = {'host': '0.0.0.0', 'port': 5000}
    if getenv('HBNB_API_HOST'):
        env_var['host'] = getenv('HBNB_API_HOST')
    if getenv('HBNB_API_PORT'):
        env_var['port'] = int(getenv('HBNB_API_PORT'))
    app.run(host=env_var.get('host'), port=env_var.get('port'))

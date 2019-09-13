#!/usr/bin/python3
"""City Class"""

from models import storage
from api.v1.views import app_views
from flask import Flask, abort, make_response, jsonify, request
from os import getenv
from models.state import State
from models.city import City


@app_views.route('/api/v1/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_city():
    """retrieve city list (var = st_list) from json"""
    city_list = [obj.to_dict() for obj in storage.all('City').values()]
    if state is None:
        abort(404)
    return jsonify(city_list)


@app_views.route('/api/v1/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_cityId(city_id):
    """retrieve state objects with id"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id',
                 methods=['DELETE'], strict_slashes=False)
def del_stateId(state_id):
    """delete state object if given state id"""
    state = storage.get('state', state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """create a dict from HTTP body request"""
    """new state object"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if not 'name' in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    object_data = request.get_json()
    object = State(**object_data)
    object.save()
    return jsonify(object.to_dict()), 201


@app_views.route('/states/<string:state_id',
                 methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """update state obj with key value pair"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    object = storage.get('State', state_id)
    if object is None:
        abort(404)
    object_data = request.get_json()
    object.name = object_data['name']
    object.save()
    return jsonify(object.to_dict()), 200

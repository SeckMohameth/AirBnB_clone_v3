#!/usr/bin/python3
"""City Class"""

from models import storage
from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models.city import City


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_city(state_id):
    """retrieve city list (var = st_list) from json"""
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    city_list = [obj.to_dict() for obj in state.cities]
    return jsonify(city_list), 200


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_cityId(city_id):
    """retrieve state objects with id"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict()), 200


@app_views.route('/city/<city_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_city(city_id):
    """delete state object if given state id"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """create a dict from HTTP body request"""
    """new state object"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if not 'name' in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    object_data = request.get_json()
    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    object_data['state_id'] = state.id
    object = City(**object_data)
    object.save()
    return jsonify(object.to_dict()), 201


@app_views.route('/cities/<city_id>',
                 methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """update state obj with key value pair"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    object = storage.get('City', city_id)
    if object is None:
        abort(404)
    object_data = request.get_json()
    object.name = object_data['name']
    object.save()
    return jsonify(object.to_dict()), 200

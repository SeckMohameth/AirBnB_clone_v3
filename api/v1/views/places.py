#!/usr/bin/python3
"""Place Class"""
from models import storage
from models.place import Place
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_place(city_id):
    """retrieve places in city (var = pl_list) from json"""
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    pl_list = [p_obj.to_dict() for p_obj in city.places]
    return jsonify(p_list)


@app_views.route('/places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def get_placeId(place_id):
    """retrieve place objects with id"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_placeId(place_id):
    """delete place object if given id"""
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/places', methods=['POST'], strict_slashes=False)
def create_place():
    """create a dict from HTTP body request"""
    """new place object"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if not 'name' in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    if not 'user_id' in request.get_json()
        return jsonify({"error": "Missing user_id"}), 400
    else:
    object_data = request.get_json()
    city = storage.get('City', city_id)
    user = storage.get('User', obj_data['user_id'])
    if city in None or user is None:
        abort(404)
    obj_data['city_id'] = city.id
    obj_data['user_id'] = user.id
    object = Place(**object_data)
    object.save()
    return jsonify(object.to_dict()), 201


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """update place obj with key value pair"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    object = storage.get('Place', place_id)
    if object is None:
        abort(404)
    object_data = request.get_json()
    ignore = ("id", "user_id", "create_at", "update_at")
    for p, q in obj_data.items():
        if p in ignore:
            pass
    else:
        setattr(obj, p, q)
    object.save()
    return jsonify(object.to_dict()), 200

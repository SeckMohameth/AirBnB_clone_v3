#!/usr/bin/python3
"""
Amenity Class
"""

from models import storage
from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from models.amenity import Amenity


@app_views.route('amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """retrieve amenities list (var = a_list) from json"""
    a_list = [a_obj.to_dict() for a_obj in storage.all('Amenity').values()]
    return jsonify(a_list)


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def get_amenityId(amenity_id):
    """retrieve amenity objects with amenity id"""
    amenity = storage.get('Amenity', amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_amenityId(amenity_id):
    """delete amenity object if given amenity id"""
    amenity = storage.get('Amenity', amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """create a dict from HTTP body request"""
    """new amenity object"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if not 'name' in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    object_data = request.get_json()
    object = Amenity(**object_data)
    object.save()
    return jsonify(object.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def update_amenity(amenities_id):
    """update state obj with key value pair"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    object = storage.get('Amenity', amenity_id)
    if object is None:
        abort(404)
    object_data = request.get_json()
    object.name = object_data['name']
    object.save()
    return jsonify(object.to_dict()), 200

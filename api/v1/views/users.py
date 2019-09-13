#!/usr/bin/python3
"""User Class"""
from models import storage
from models.user import User
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """retrieve users list (var = u_list) from json"""
    u_list = [u_obj.to_dict() for u_obj in storage.all('User').values()]
    return jsonify(u_list)


@app_views.route('/users/<user_id>',
                 methods=['GET'], strict_slashes=False)
def get_userId(user_id):
    """retrieve user objects with id"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_userId(user_id):
    """delete user object if given id"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """create a dict from HTTP body request"""
    """new user object"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    if not 'name' in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    object_data = request.get_json()
    object = User(**object_data)
    object.save()
    return jsonify(object.to_dict()), 201


@app_views.route('/users/<user_id>',
                 methods=['PUT'], strict_slashes=False)
def update_user(users_id):
    """update user obj with key value pair"""
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    object = storage.get('User', user_id)
    if object is None:
        abort(404)
    object_data = request.get_json()
    ignore = ("id", "email", "create_at", "update_at")
    for u in obj_data.keys():
        if u in ignore:
            pass
    else:
        setattr(obj, u, object_data[u])
    object.save()
    return jsonify(object.to_dict()), 200

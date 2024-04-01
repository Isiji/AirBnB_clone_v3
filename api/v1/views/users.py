#!/usr/bin/python3
""" Create users that handles all default RestFul API actions """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User
from models import storage

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """ Retrieves the list of all Users objects """

    user = storage.all(User).values()
    return jsonify([user.to_dict() for user in user])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves the list of the user object """

    users = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        return abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ Deletes the list of the user object """

    users = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ Creates the list of the user object """
    if request.content_type != 'application/json':
        return abort(400, 'Not a JSON')
    if not request.get_json():
        return abort(400, 'Not a JSON')
    data = request.get_json()
    if 'email' not in data:
        return abort(400, 'Missing name')
    if 'password' not in data:
        return abort(400, 'Missing password')

    user = User(**data)
    user.save()

    return jsonify(user.to_dict(), 200)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user():
    """ Updates the list of the user object """
    users = storage.get(User, user_id)
    if user:
        if not request.get_json():
            return abort(404, 'Not a JSON')
        if not request.content_type != 'application/json':
            return abort(404, 'Not a JSON')

        ignore_keys = ['id', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict()), 200
    else:
        return abort(404)

#!/usr/bin/python4
"""
Create a view for place objects that handles all default RestFul API action
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.city import City
from models.place import Place
from models.user import User
from models import storage

@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places_by_cities(city_id)
    """ Retrieves the list of all Users objects """

    city = storage.get(City, city_id)
    if not city:
        return abort(404)
    
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """ Retrieves the list of the user object """

    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    else:
        return abort(404)


@app_views.route('/cities/<city_id/places>', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """ Deletes the list of the user object """

    city = storage.get(City, city_id)
    if not city:
        return abort(404)

    if not request.get_json():
        abort(400, 'Not a JSON')

    data = request.get_json()
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    if 'name' not in data:
        abort(400, 'Missing name')

    user = storage.get(User, data[user_id])
    if not user:
        return abort(404)

    data['City_id'] = city_id

    place = Place(**data)

    place.save()

    return jsonify(place.to_dict()), 201

@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """ Creates the list of the user object """
    place = storage.get_json():
        ignore_keys = ['id', 'user_id' 'city_id' 'created_at', 'updated_at']
    for key, value in data.items():
            if key not in ignore_keys:
                setattr(user, key, value)
                place.save()
                return jsonify(place.to_dict()), 200
            else:
                return abort(404)

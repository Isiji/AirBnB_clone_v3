#!/usr/bin/python3
""" This module defines routes for handling places related HTTP requests """

from api.v1.views import app_views
from flask import jsonify, request, abort
from models.city import City
from models.place import Place
from models.user import User
from models import storage

@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """ Retrieves a list of places associated with a specific city """

    # Retrieve the City object associated with the provided city_id from the storage
    city = storage.get(City, city_id)
    
    # If the city object doesn't exist, return a 404 Not Found error
    if not city:
        return abort(404)

    # Retrieve all places from the storage
    places = storage.all(Place).values()

    # Filter places to include only those associated with the specified city_id
    places = [place.to_dict() for place in places if place.city_id == city_id]

    # Return the list of places as a JSON response
    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """ Retrieves a place based on its ID """

    # Retrieve the Place object associated with the provided place_id from the storage
    place = storage.get(Place, place_id)
    
    # If the place object exists, return its data as a JSON response
    if place:
        return jsonify(place.to_dict())
    
    # If the place object doesn't exist, return a 404 Not Found error
    else:
        return abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """ Deletes a place based on its ID """

    # Retrieve the Place object associated with the provided place_id from the storage
    place = storage.get(Place, place_id)
    
    # If the place object doesn't exist, return a 404 Not Found error
    if not place:
        return abort(404)

    # Delete the place object from the storage
    storage.delete(place)
    storage.save()

    # Return an empty JSON response with a 200 OK status code
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def create_place(city_id):
    """ Creates a new place associated with a specific city """

    # Retrieve the City object associated with the provided city_id from the storage
    city = storage.get(City, city_id)
    
    # If the city object doesn't exist, return a 404 Not Found error
    if not city:
        return abort(404)

    # Check if the request contains JSON data
    if not request.get_json():
        abort(400, 'Not a JSON')

    # Parse JSON data from the request
    data = request.get_json()

    # Ensure that the required fields (user_id and name) are present in the JSON data
    if 'user_id' not in data or 'name' not in data:
        abort(400, 'Missing required fields')

    # Retrieve the User object associated with the provided user_id from the storage
    user = storage.get(User, data['user_id'])
    
    # If the user object doesn't exist, return a 404 Not Found error
    if not user:
        return abort(404)

    # Add the city_id to the JSON data
    data['city_id'] = city_id

    # Create a new Place object using the JSON data
    place = Place(**data)

    # Save the new place object to the storage
    place.save()

    # Return the newly created place data as a JSON response with a 201 Created status code
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def update_place(place_id):
    """ Updates a place based on its ID """

    # Retrieve the Place object associated with the provided place_id from the storage
    place = storage.get(Place, place_id)
    
    # If the place object doesn't exist, return a 404 Not Found error
    if not place:
        return abort(404)

    # List of keys to ignore when updating the place object
    ignore_keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

    # Update the place object attributes with the JSON data from the request
    for key, value in request.get_json().items():
        
        # Check if the key is not in the ignore list
        if key not in ignore_keys:
            
            # Set the attribute value for the place object
            setattr(place, key, value)
            
            # Save the changes to the storage
            place.save()
            
            # Return the updated place data as a JSON response with a 200 OK status code
            return jsonify(place.to_dict()), 200
        
        # If the key is in the ignore list, return a 404 Not Found error
        else:
            return abort(404)

#!/usr/bin/python3
""" Index module """
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"}), 200

@app.views.rout('/stats')
def get_stats():
    """ Retrieves the number of each objects by type """
    stats = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User'),
            }

    return jsonify(stats)

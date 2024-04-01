#!/usr/bin/python3
""" Index module """
from api.v1.views import app_views
from flask import jsonify
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return status"""
    return jsonify({"status": "OK"}), 200
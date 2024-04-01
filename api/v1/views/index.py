from api.v1.views.index import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    return status
    """
    return jsonify({"status": "OK"})
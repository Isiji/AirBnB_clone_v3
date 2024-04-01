#!/usr/bin/python3
""" Main file """
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(exception):
    storage.close()

@app.errorhandler(404)
def not found(error)
""" Handler for 404 errors that returns a JSON-formatted 404 status code response. """
response = {"error": "Not found"}
return jsonify(response), 404

if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = getenv('HBNB_API_PORT', 5000)
    app.run(host=HOST, port=PORT, threaded=True)

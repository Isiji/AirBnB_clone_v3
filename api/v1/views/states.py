#!/usr/bin/python3
""" State module for retrieving apis """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Return all states"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states.values()])

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieve a State object by state_id.
    
    Retrieves a State object corresponding to the given state_id.
    
    Args:
        state_id (str): The ID of the state to retrieve.
        
    Returns:
        json: A JSON representation of the State object.
        
    Raises:
        404: If the state_id is not linked to any State object.
    """
    # Retrieve the State object from storage
    
    state = storage.get(State, state_id)

    #check if state is not linked to the given id
    if state is None:
        abort(404, description="State Not found")
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object by state_id.
    
    Deletes a State object corresponding to the given state_id.
    
    Args:
        state_id (str): The ID of the state to delete.
        
    Returns:
        json: An empty dictionary.
        
    Raises:
        404: If the state_id is not linked to any State object.
    """
    # Retrieve the State object from storage
    state = storage.get(State, state_id)

    #check if state is not linked to the given id
    if state is None:
        abort(404, description="State Not found")
    storage.delete(state)
    storage.save()
    return jsonify({}, status=200)

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """Creates a new State object.
    
    Creates a new State object with the data passed in the request.
    
    Returns:
        json: A JSON representation of the new State object.
    """
    data = request.get_json()
    if data is None:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict(), status=201)

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """Updates a State object by state_id.
    
    Updates a State object corresponding to the given state_id with the data
    passed in the request.
    
    Args:
        state_id (str): The ID of the state to update.
        
    Returns:
        json: A JSON representation of the updated State object.
        
    Raises:
        404: If the state_id is not linked to any State object.
    """
    data = request.get_json()
    if data is None:
        abort(400, description="Not a JSON")
    state = storage.get(State, state_id)
    if state is None:
        abort(404, description="State Not found")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
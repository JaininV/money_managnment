from flask import Blueprint, jsonify
from controller.shift import getShiftData, addShift, updateShitTime, deleteShift

shift_blueprint = Blueprint('expense', __name__)
 

@shift_blueprint.route('/shift/add', methods=['POST'])
def add_shift_api():
    try:
        data = addShift()
        return data 
    except Exception as err:
        return f"Error: {err}"

@shift_blueprint.route('/shift/edit', methods=['PUT'])
def update_shift_api():
    try:
        data = updateShitTime()
        return data
    except Exception as err:
        return f"Error: {err}"
    
# Delete shift
@shift_blueprint.route('/shift/delete', methods=['DELETE'])
def delete_shift_api():
    try:
        data = deleteShift()
        return data
    except Exception as err:
        return f"Error: {err}"
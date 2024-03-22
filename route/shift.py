from flask import Blueprint, jsonify
from controller.shift import getShiftData, addShift, updateShitTime

shift_blueprint = Blueprint('shifts', __name__)
 

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
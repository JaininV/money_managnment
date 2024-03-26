from flask import Blueprint, jsonify
from controller.income import getShiftData, addShift, updateShitTime

income_blueprint = Blueprint('income', __name__)
 

@income_blueprint.route('/shift/add', methods=['POST'])
def add_shift_api():
    try:
        data = addShift()
        return data 
    except Exception as err:
        return f"Error: {err}"

@income_blueprint.route('/shift/edit', methods=['PUT'])
def update_shift_api():
    try:
        data = updateShitTime()
        return data
    except Exception as err:
        return f"Error: {err}"
from flask import Blueprint, jsonify
from controller.expense import getShiftData, addShift, updateShitTime, deleteShift

expense_blueprint = Blueprint('expense', __name__)
 

@expense_blueprint.route('/expense/add', methods=['POST'])
def add_shift_api():
    try:
        data = addShift()
        return data 
    except Exception as err:
        return f"Error: {err}"
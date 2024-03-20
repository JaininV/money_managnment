from flask import Blueprint, jsonify
from controller.shift import getShiftData, addShift, updateShitTime

shift_blueprint = Blueprint('shifts', __name__)
 

@shift_blueprint.route('/shift/add', methods=['POST'])
def add_shift_api():
    # Your API logic here
    data = addShift()
    return data

@shift_blueprint.route('/shift/edit', methods=['POST'])
def add_shift_api():
    # Your API logic here
    data = updateShitTime()
    # function retuen
    return data
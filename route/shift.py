from flask import Blueprint, jsonify
from controller.shift import getShiftData, addShift, updateShitTime

shift_blueprint = Blueprint('shifts', __name__)
 

@shift_blueprint.route('/shift/add', methods=['POST'])
def add_shift_api():
    data = addShift()
    return data

@shift_blueprint.route('/shift/edit', methods=['POST'])
def add_shift_api():
    data = updateShitTime()
    return data
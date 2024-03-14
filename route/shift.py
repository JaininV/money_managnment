from flask import Blueprint, jsonify
from controller.shift import getShiftData, addShift

shift_blueprint = Blueprint('shifts', __name__)
 

@shift_blueprint.route('/shift/add', methods=['POST'])
def add_shift_api():
    # Your API logic here
    data = addShift()
    return data


from flask import Blueprint, jsonify
from controller.shift import getShiftData

shift_blueprint = Blueprint('shifts', __name__)
 

@shift_blueprint.route('/shift/', methods=['GET'])
def get_shift_data_api():
    # Your API logic here
    data = getShiftData()
    return data

from flask import Blueprint, jsonify
from controller.shift import getShiftData, addJob, updateJob, deleteJob

shift_blueprint = Blueprint('shifts', __name__)
 

@shift_blueprint.route('/shift/', methods=['GET'])
def get_shift_data_api():
    # Your API logic here
    data = getShiftData()
    return data

@shift_blueprint.route('/shift/add_job', methods=['POST'])
def add_job_api():
    # Your API logic here
    data = addJob()
    return data 

@shift_blueprint.route('/shift/edit_job', methods=['PUT'])
def update_job_api():
    # Your API logic here
    data = updateJob()
    return data 

@shift_blueprint.route('/shift/delete_job', methods=['DELETE'])
def delete_job_api():
    # Your API logic here
    data = deleteJob()
    return data 
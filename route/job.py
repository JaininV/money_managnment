from flask import Blueprint, jsonify
from controller.job import getShiftData, addJob, updateJob, deleteJob

job_blueprint = Blueprint('jobs', __name__)
 

@job_blueprint.route('/job/', methods=['GET'])
def get_job_data_api():
    # Your API logic here
    data = getShiftData()
    return data

@job_blueprint.route('/job/add', methods=['POST'])
def add_job_api():
    # Your API logic here
    data = addJob()
    return data 

@job_blueprint.route('/job/edit', methods=['PUT'])
def update_job_api():
    # Your API logic here
    data = updateJob()
    return data 

@job_blueprint.route('/job/delete', methods=['DELETE'])
def delete_job_api():
    # Your API logic here
    data = deleteJob()
    return data 
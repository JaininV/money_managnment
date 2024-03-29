from flask import Blueprint, jsonify
from controller.users import userData, addUser, updateUser, deleteUser

user_blueprint = Blueprint('users', __name__)
 

@user_blueprint.route('/user/', methods=['GET'])
def user_data_api():
    # Your API logic here
    data = userData()
    return data

@user_blueprint.route('/user/add', methods=['POST'])
def add_User(): 
    # Your API logic here
    data = addUser()
    return data
 
@user_blueprint.route('/user/edit', methods=['PUT'])
def update_user():
    # Your API logic here
    data = updateUser()
    return data

@user_blueprint.route('/user/delete', methods=['DELETE'])
def delete_user():
    # Your API logic here
    data = deleteUser()
    return data
 
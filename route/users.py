from flask import Blueprint, jsonify
from controller.users import userData, addUser

user_blueprint = Blueprint('users', __name__)
 

@user_blueprint.route('/users', methods=['GET'])
def user_data_api():
    # Your API logic here
    data = userData()
    return data

@user_blueprint.route('/user/add', methods=['POST'])
def add_User():
    # Your API logic here
    data = addUser()
    return data
 
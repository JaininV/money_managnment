from flask import Blueprint, jsonify
from controller.login import loginUser, loginCheck

login_blueprint = Blueprint('login', __name__)
 

@login_blueprint.route('/login/', methods=['GET'])
def login_user_api():
    # Your API logic here
    data = loginUser()
    return data

@login_blueprint.route('/login/check', methods=['GET'])
def login_check_api():
    # Your API logic here
    data = loginCheck()
    return data
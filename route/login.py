from flask import Blueprint, jsonify
from controller.login import loginUser

login_blueprint = Blueprint('login', __name__)
 

@login_blueprint.route('/login/', methods=['GET'])
def user_data_api():
    # Your API logic here
    data = loginUser()
    return data
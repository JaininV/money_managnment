from flask import Flask, render_template, jsonify, request, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request


from db_connection import connection, cursor
from datetime import datetime
import json

# Simulated async function
def loginUserApi(data):
    try:
        userid = data['userid']
        password = data['password']

        cursor.execute("SELECT * FROM user_details WHERE unique_id = %s AND status = %s",(userid, 'active'))
        results = cursor.fetchone()
        connection.commit()

        if results is not None:
            cursor.execute("SELECT * FROM user_details WHERE unique_id = %s AND password = %s AND status = %s",(userid, password, 'active'))
            results = cursor.fetchone()
            connection.commit()

            if results is not None:
                try:    
                    token_gen = create_access_token(identity=userid)

                    return jsonify(access_token=token_gen)
                except Exception as e:
                    return f"Error: {str(e)}"
                
            else:
                return "Password is incorrect"
        
        else:
            return 'User is not exist'

    except Exception as e:
        return f"Error: {str(e)}"

def loginCheckApi():
    verify_jwt_in_request()
    current_user = get_jwt_identity()
    
    return {'user': current_user}
 

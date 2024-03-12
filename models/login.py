from flask import Flask, render_template, jsonify, request, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from db_connection import connection, cursor
import datetime
import json

# Simulated async function
def loginUserApi(data):
    try:
        userid = data['userid']
        password = data['password']

        cursor.execute("SELECT * FROM user_details WHERE status = 'active'")
        results = cursor.fetchall()
        print(results)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    return {'data': data}
 

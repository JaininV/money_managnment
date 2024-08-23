from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
from models.login import loginCheckApi
from datetime import datetime
import calendar

# get all jobs
     
# Add new jobs
def addShiftApi(data):
    try:
        token = loginCheckApi()
        user_id = token['user']
        name = data['name']
        
        return{
            'TOken': user_id,
            'Name': name
        }       
        
    except Exception as e:
        
        return f"Error: {str(e)}"
    


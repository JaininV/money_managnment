from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
from models.login import loginCheckApi
import datetime
import json

# Simulated async function
def getShiftDataApi():
    try:
        userid = loginCheckApi()
        return {'user_id': userid['user']}
        
    except Exception as e:
        return f"Error: {str(e)}"
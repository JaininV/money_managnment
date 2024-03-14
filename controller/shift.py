#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.shift import getShiftDataApi, addShiftApi
import asyncio
 
def getShiftData():
    try: 
        page = getShiftDataApi()
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"
    
# Add shift
def addShift():
    try: 
        data = request.form
        page = addShiftApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"
#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.shift import getShiftDataApi, addShiftApi, updateShiftTimeApi, deleteShiftApi
import asyncio
 
def getShiftData():
    try: 
        page = getShiftDataApi()
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"
    
# Add shift
def addShift():
    # funciton
    try: 
        data = request.form
        page = addShiftApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"
    
# Add shift
def updateShitTime():
    try: 
        data = request.form
        page = updateShiftTimeApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

# Delete shift
def deleteShift():
    try:
        data = request.form
        page = deleteShiftApi(data)
        return page
    
    except Exception as e:
        print("I am back baby")
        return f"Error: {str(e)}"

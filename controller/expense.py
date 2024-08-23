#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.expense import addShiftApi
import asyncio
    
# Add shift
def addShift():
    # funciton
    try: 
        data = request.form
        page = addShiftApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"
    

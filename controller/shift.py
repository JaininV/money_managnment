#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.shift import getShiftDataApi
import asyncio
 
def getShiftData():
    try: 
        page = getShiftDataApi()
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

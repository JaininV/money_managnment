#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.job import getShiftDataApi, addJobApi, updateJobApi, deleteJobApi
import asyncio
 
def getShiftData():
    try: 
        page = getShiftDataApi()
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

# Add new job
def addJob():
    try: 
        data = request.form
        page = addJobApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

# Update job
def updateJob():
    try: 
        data = request.form
        page = updateJobApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

# Delete job
def deleteJob():
    try: 
        data = request.form
        page = deleteJobApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"
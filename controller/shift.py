#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.users import getDataApi, addUserApi, updateDataApi, deleteDataApi
import asyncio
 
def userData(): 
    user_data = getDataApi()
    return user_data

def addUser():
    data = request.form
    page = addUserApi(data)
    return page

def updateUser():
    try: 
        data = request.form
        page = updateDataApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

def deleteUser():
    try: 
        data = request.form
        page = deleteDataApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

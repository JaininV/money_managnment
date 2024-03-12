#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.login import loginUserApi
import asyncio
 
def loginUser():
    try: 
        data = request.form
        page = loginUserApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.login import loginUserApi, loginCheckApi
import asyncio
 
def loginUser():
    try: 
        data = request.form
        page = loginUserApi(data)
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

def loginCheck():
    try: 
        page = loginCheckApi()
        return page
    
    except Exception as e:
        return f"Error: {str(e)}"

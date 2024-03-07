#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.users import getDataApi, addUserApi
import asyncio
 
def userData(): 
    user_data = getDataApi()
    return user_data

def addUser():
    data = request.form
    page = addUserApi(data)
    return page
 
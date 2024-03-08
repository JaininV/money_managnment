from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
import datetime
import json

# Simulated async function
def getDataApi():
    try:
        cursor.execute("SELECT * FROM user_details WHERE status = 'active'")
        results = cursor.fetchall()
        print(results)
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    return {'data': results}
 
def addUserApi(data):
    first_name = data['first_name']
    last_name = data['last_name']
    email_id = data['email_id']
    bank_name = data['bank_name']
    number_of_job = data['number_of_job']
    job_name = data['job_name']
    rent_or_insaurance = data['rent_or_insaurance']
    amount_rent_insaurance =data['amount_rent_insaurance']
    car_or_transit =data['car_or_transit']
    amount_car_transit =data['amount_car_transit']
    phone_bill = data['phone_bill']
    password = data['password']

    # cursor = connection.cursor()
    
    cursor.execute("SELECT * From user_details where first_name = %s AND last_name = %s WHERE status = 'active'", (first_name, last_name))
    check = cursor.fetchone()
    connection.commit()
    

    if check is None:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        
        query = "INSERT INTO user_details (first_name, last_name, email_id, bank_name, number_of_job, job_name, rent_or_insaurance, amount_rent_insaurance, car_or_transit, amount_car_transit, phone_bill, password, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (first_name, last_name, email_id, bank_name, number_of_job, job_name, rent_or_insaurance, amount_rent_insaurance, car_or_transit, amount_car_transit, phone_bill, password, formatted_datetime, formatted_datetime)

        try:
            cursor.execute(query, value)
            results = connection.commit()
            cursor.close()
            connection.close()
            return f'Welcome {first_name},'
        
        except Exception as e:
            return f"Error: {str(e)}"
        
    else:
        return "Data already exits"

def updateDataApi(data):
    try:
        id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        email_id = data['email_id']
        bank_name = data['bank_name']
        number_of_job = data['number_of_job']
        job_name = data['job_name']
        rent_or_insaurance = data['rent_or_insaurance']
        amount_rent_insaurance =data['amount_rent_insaurance']
        car_or_transit =data['car_or_transit']
        amount_car_transit =data['amount_car_transit']
        phone_bill = data['phone_bill']
        password = data['password']

        cursor.execute("SELECT id, first_name, last_name From user_details where id = %s AND email_id = %s WHERE status = 'active'", (id, email_id))
        check = cursor.fetchone()
        connection.commit()
        
        # Check user exit or not
        if check is None:
            return f"User is not exit!"
        
        else:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            query = "UPDATE user_details SET first_name = %s, last_name = %s, email_id = %s, bank_name = %s, number_of_job = %s, job_name = %s, rent_or_insaurance = %s, amount_rent_insaurance = %s, car_or_transit = %s, amount_car_transit = %s, phone_bill = %s, password = %s, updated_at = %s WHERE id = %s"
            value = (first_name, last_name, email_id, bank_name, number_of_job, job_name, rent_or_insaurance, amount_rent_insaurance, car_or_transit, amount_car_transit, phone_bill, password, formatted_datetime, id)

            # Execute query
            try:
                cursor.execute(query, value)
                results = connection.commit()
                cursor.close()
                connection.close()
                return f'{first_name}, data is updated!'
        
            except Exception as e:
                return f"Error: {str(e)}"

    except Exception as e:
        return f"Error: {str(e)}"
    
def deleteDataApi(data):
    try:
        id = data['id']
        email_id = data['email_id']
        status = 'inactive'
        cursor.execute("SELECT id, first_name, last_name From user_details where id = %s AND email_id = %s AND status = 'active'", (id, email_id))
        check = cursor.fetchone()
        connection.commit()

        if check is not None:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            query = "UPDATE user_details SET status = %s, updated_at = %s WHERE id = %s"
            value = (status, formatted_datetime, id)

            try:
                cursor.execute(query, value)
                results = connection.commit()
                cursor.close()
                connection.close()
                return f'data is Deleted!'
        
            except Exception as e:
                return f"Error: {str(e)}"
        
        else:
            return f"User is not exit or information is invalid!"
        
    except Exception as e:
        return f"Error: {str(e)}"
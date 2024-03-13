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
    unique_id = data['unique_id']
    bank_name = data['bank_name']
    number_of_job = data['number_of_job']
    job_name = data['job_name']
    rent_or_insaurance = data['rent_or_insaurance']
    amount_rent_insaurance =data['amount_rent_insaurance']
    car_or_transit =data['car_or_transit']
    amount_car_transit =data['amount_car_transit']
    phone_bill = data['phone_bill']
    password = data['password']
    
    # Get data for verification
    cursor.execute("SELECT id, first_name, last_name, unique_id From user_details where email_id = %s OR unique_id = %s AND status = 'active'", (email_id, unique_id))
    check = cursor.fetchone()
    connection.commit()

    if check is None:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        
        # Inser user data query
        insert_query = "INSERT INTO user_details (first_name, last_name, email_id, unique_id, bank_name, number_of_job, job_name, rent_or_insaurance, amount_rent_insaurance, car_or_transit, amount_car_transit, phone_bill, password, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (first_name, last_name, email_id, unique_id, bank_name, number_of_job, job_name, rent_or_insaurance, amount_rent_insaurance, car_or_transit, amount_car_transit, phone_bill, password, formatted_datetime, formatted_datetime)
        
        # Create job table query
        job_table = """
                        CREATE TABLE  {}_job (
                        job_id INT(10) NOT NULL AUTO_INCREMENT,
                        job_name VARCHAR(45) NOT NULL,
                        wage INT(45) NOT NULL DEFAULT 16.55,
                        status varchar(10) NOT NULL DEFAULT 'active',
                        created_at DATETIME NOT NULL,
                        updated_at DATETIME NOT NULL,
                        PRIMARY KEY (`job_id`)
                    );
                    """.format(unique_id)
        
        # Shift table query
        shift_table = """
                        CREATE TABLE  {}_shift (
                            shift_id INT(10) NOT NULL AUTO_INCREMENT,
                            job_id VARCHAR(45) NOT NULL,
                            shift_day  varchar(45) NOT NULL,  
                            shift_start_time DATETIME NOT NULL,
                            shift_end_time DATETIME NOT NULL,
                            total_hours INT(10) NOT NULL,
                            pay INT(10) NOT NULL,
                            PRIMARY KEY (`shift_id`)
                        );
                        """.format(unique_id)
        
        # Income table query
        income_table = """
                        CREATE TABLE  {}_income (
                            income_id INT(10) NOT NULL AUTO_INCREMENT,
                            job_id INT(45) NOT NULL,
                            date DATETIME NOT NULL,
                            total_amount INT(10) NOT NULL,
                            PRIMARY KEY (`income_id`)
                        );
                        """.format(unique_id)
        
        # Expense query
        expense_table = """
                        CREATE TABLE  {}_expense (
                            expense_id INT(10) NOT NULL AUTO_INCREMENT,
                            expense_on VARCHAR(45) NOT NULL,
                            type VARCHAR(45) NOT NULL,
                            total_amount INT(10) NOT NULL,
                            date DATETIME NOT NULL,
                            PRIMARY KEY (`expense_id`)
                        );
                        """.format(unique_id)
        
        try:
            # Execute each query
            cursor.execute(insert_query, value)
            results = connection.commit()
            
            cursor.execute(job_table)
            connection.commit()

            cursor.execute(shift_table)
            connection.commit()

            cursor.execute(income_table) 
            connection.commit()

            cursor.execute(expense_table)
            connection.commit()
            
            cursor.close()
            connection.close()
            return f'Welcome {first_name},'
        
        except Exception as e:
            return f"Error: {str(e)}"
        
    else:
        return "Data already exits"

def updateDataApi(data):
    try:
        first_name = data['first_name']
        last_name = data['last_name']
        unique_id = data['unique_id']
        bank_name = data['bank_name']
        number_of_job = data['number_of_job']
        job_name = data['job_name']
        rent_or_insaurance = data['rent_or_insaurance']
        amount_rent_insaurance =data['amount_rent_insaurance']
        car_or_transit =data['car_or_transit']
        amount_car_transit =data['amount_car_transit']
        phone_bill = data['phone_bill']
        password = data['password']

        cursor.execute("SELECT id, first_name, last_name From user_details where unique_id = %s AND status = %s", (unique_id, 'active'))
        check = cursor.fetchone()
        connection.commit()
        
        # Check user exit or not
        if check is None:
            return f"User is not exit!"
        
        else:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            query = "UPDATE user_details SET first_name = %s, last_name = %s, bank_name = %s, number_of_job = %s, job_name = %s, rent_or_insaurance = %s, amount_rent_insaurance = %s, car_or_transit = %s, amount_car_transit = %s, phone_bill = %s, password = %s, updated_at = %s WHERE unique_id = %s"
            value = (first_name, last_name, bank_name, number_of_job, job_name, rent_or_insaurance, amount_rent_insaurance, car_or_transit, amount_car_transit, phone_bill, password, formatted_datetime, unique_id)

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
        unique_id = data['unique_id']
        email_id = data['email_id']
        status = 'inactive'
        cursor.execute("SELECT id, first_name, last_name From user_details where unique_id = %s AND email_id = %s AND status = 'active'", (unique_id, email_id))
        check = cursor.fetchone()
        connection.commit()

        if check is not None:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            query = "UPDATE user_details SET status = %s, updated_at = %s WHERE unique_id = %s"
            value = (status, formatted_datetime, unique_id)

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
from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
from models.login import loginCheckApi
import datetime
import json

# get all jobs
def getShiftDataApi():
    try:
        token = loginCheckApi()
        user_id = token['user']
        query = """
                    SELECT job_id, job_name, wage
                    FROM {}_job
                    WHERE status = 'active'
                """.format(user_id)
        
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()

        return {'data': result}
        
    except Exception as e:
        return f"Error: {str(e)}"
    
# Add new jobs
def addJobApi(data):
    try:
        token = loginCheckApi()
        user_id = token['user']
        job_name = data['job_name']
        wage = data['wage']
        
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        check_query = """
                        SELECT job_id
                        FROM {}_job
                        WHERE job_name = '{}'
                        """.format(user_id, job_name)
        
        cursor.execute(check_query)
        check = cursor.fetchone()
        connection.commit()
        
        if check is None:
            insert_query = """
                            INSERT INTO {}_job
                            (job_name, wage, created_at, updated_at)
                            VALUES ('{}', {}, '{}', '{}')
                            """.format(user_id, job_name, wage, formatted_datetime, formatted_datetime,)
            values = (user_id, job_name, wage, formatted_datetime, formatted_datetime,)
            cursor.execute(insert_query)
            result = connection.commit()

            return {
                    'API execute time': formatted_datetime,
                    'data': result,
                    'login user': user_id
                    }
        
        else:
            return f"Data already exists"
    except Exception as e:
        return f"Error: {str(e)}"

# Update data
def updateJobApi(data):
    try:
        token = loginCheckApi()
        user_id = token['user']
        wage = data['wage']
        job_name = data['job_name']        
        
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        check_query = """
                        SELECT job_id
                        FROM {}_job
                        WHERE job_name = '{}'
                        """.format(user_id, job_name)
        
        cursor.execute(check_query)
        check = cursor.fetchone()
        connection.commit()
        
        if check is not None:
            update_query = """
                            UPDATE {}_job 
                            SET wage = {}, updated_at = '{}'
                            WHERE status = 'active'
                            """.format(user_id, wage, formatted_datetime)
            
            cursor.execute(update_query)
            result = connection.commit()

            return {
                    'API execute time': formatted_datetime,
                    'data': result,
                    'login user': user_id
                    }
        
        else:
            return f"Data not exist"
        
    except Exception as e:
        return f"Error: {str(e)}"
    
# Delete job data
def deleteJobApi(data):
    try:
        token = loginCheckApi()
        user_id = token['user']
        job_name = data['job_name']        
        
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        check_query = """
                        SELECT job_id
                        FROM {}_job
                        WHERE job_name = '{}'
                        """.format(user_id, job_name)
        
        cursor.execute(check_query)
        check = cursor.fetchone()
        connection.commit()
        
        if check is not None:
            delete_query = """
                            UPDATE {}_job 
                            SET status = '{}', updated_at = '{}'
                            WHERE job_name = '{}'
                            """.format(user_id, 'inactive', formatted_datetime, job_name)
            
            cursor.execute(delete_query)
            result = connection.commit()

            return {
                    'API execute time': formatted_datetime,
                    'data': result,
                    'login user': user_id
                    }
        
        else:
            return f"Data not exist"
        
    except Exception as e:
        return f"Error: {str(e)}"
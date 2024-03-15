from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
from models.login import loginCheckApi
from datetime import datetime
import calendar
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
def addShiftApi(data):
    try:
        token = loginCheckApi()
        user_id = token['user']
        start_time = data['start_time']
        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        ts = datetime.timestamp(start_time)
        shift_date = start_time.date()
        end_time = data['end_time']
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        diff = end_time - start_time
        days, seconds = diff.days, diff.seconds
        total_hour = days * 24 + seconds / 3600
        job_name = data['job']
        
        # take id from job tabel
        job_id_query = """
                    SELECT job_id, wage 
                    FROM {}_job
                    WHERE job_name = '{}' AND status = 'active'
                    """.format(user_id, job_name)
        
        cursor.execute(job_id_query)
        job_id = cursor.fetchone()
        connection.commit()

        # Arrange data for insert query
        total_pay = total_hour*job_id[1]
        week_day = calendar.day_name[start_time.weekday()]

        check  = """
                    SELECT job_id, shift_day, shift_date, shift_start_time, shift_end_time, time_timestamp, total_hours
                    FROM {}_shift 
                    WHERE shift_date = '{}'
                """.format(user_id, shift_date)
        
        # Execute check query
        cursor.execute(check)
        check_result = cursor.fetchall()
        connection.commit()
        
        if check_result is not None:
            length = len(check_result)
            count = 0
            for i in range(0, length):
                check_start_time = check_result[i][3]
                check_end_time = check_result[i][4]
                
                if check_start_time <= start_time and check_end_time >= start_time:
                    return {
                         'msg': 'You alredy have shift on this time period'
                    }

                else:
                    count += 1 
                    return 'yes'
        else:
            return 'no'
        # Executeing the query
        # insert_query = """
        #                 INSERT INTO {}_shift
        #                 (job_id, shift_day, shift_date, shift_start_time, shift_end_time, time_timestamp, total_hours, pay)
        #                 VALUES ({}, '{}', '{}', '{}', '{}', {}, {}, {})
        #                 """.format(user_id, job_id[0], week_day, shift_date, start_time, end_time, ts, total_hour, total_pay)
        
        
        # cursor.execute(insert_query)
        # connection.commit()

    except Exception as e:
        return f"Error: {str(e)}"

# Update data
def updateJobApi(data):
    try:
        token = loginCheckApi()
        user_id = token['user']
        wage = data['wage']
        job_name = data['job_name']        
        
        current_datetime = datetime.now()
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
        
        current_datetime = datetime.now()
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
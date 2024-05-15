from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
from models.login import loginCheckApi
from datetime import datetime
import calendar

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
        week_day = calendar.day_name[start_time.weekday()]
        
        # take id from job tabel
        job_id_query = """
                    SELECT job_id, wage 
                    FROM {}_job
                    WHERE job_name = '{}' AND status = 'active'
                    """.format(user_id, job_name)
        
        cursor.execute(job_id_query)
        job_id = cursor.fetchone()
        connection.commit()

        # Check job is exist or not
        if job_id is not None:    
            # Arrange data for insert query
            total_pay = total_hour*job_id[1]
            check  = """
                        SELECT job_id, shift_day, shift_date, shift_start_time, shift_end_time, time_timestamp, total_hours
                        FROM {}_shift 
                        WHERE shift_date = '{}'
                    """.format(user_id, shift_date)
            
            # Execute check query
            cursor.execute(check)
            check_result = cursor.fetchall()
            connection.commit()
            count = 0

            if check_result is not None:
                length = len(check_result)
                for i in range(0, length):
                    check_start_time = check_result[i][3]
                    check_end_time = check_result[i][4]
                    
                    if (check_start_time <= start_time and check_end_time >= start_time) or (check_start_time <= end_time and check_end_time >= end_time) or (start_time <= check_start_time and end_time >= check_start_time) or (start_time <= check_end_time and end_time >= check_end_time):
                        count = count + 1 
                        continue

                if count == 0:
                    insert_query = """
                                    INSERT INTO {}_shift
                                    (job_id, shift_day, shift_date, shift_start_time, shift_end_time, time_timestamp, total_hours, pay)
                                    VALUES({}, '{}', '{}', '{}', '{}', '{}', {}, {})
                                    """.format(user_id, job_id[0], week_day, shift_date, start_time, end_time, ts, total_hour, total_pay)
                    
                    cursor.execute(insert_query)
                    connection.commit()

                    return {
                        'msg': 'Shifte added!'
                    }
                    
                else:
                    return {
                        'msg': 'You already have shift on this time'
                    }

            else:
                insert_query = """
                                    INSERT INTO {}_shift
                                    (job_id, shift_day, shift_date, shift_start_time, shift_end_time, time_timestamp, total_hours, pay)
                                    VALUES({}, '{}', '{}', '{}', '{}', '{}', {}, {})
                                    """.format(user_id, job_id[0], week_day, shift_date, start_time, end_time, ts, total_hour, total_pay)
                    
                cursor.execute(insert_query)
                connection.commit()

                return {
                    'msg': 'Shifte added!'
                }
        else:
            return {
                'msg': 'Given job is not exist'
            }
        
    except Exception as e:
        return f"Error: {str(e)}"
    

# Update shift time
def updateShiftTimeApi(data):
    try:
        token = loginCheckApi()
        user_id = token['user']

        job = data['job']
        job_day = data['job_day']
        previous_start_time = data['previous_start_time']
        previous_end_time = data['previous_end_time']
        start_time = data['start_time']
        end_time = data['end_time']

        previous_start_time = datetime.strptime(previous_start_time, "%Y-%m-%d %H:%M:%S")
        previous_end_time = datetime.strptime(previous_end_time, "%Y-%m-%d %H:%M:%S")
        previous_start_ts = datetime.timestamp(previous_start_time)

        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        shift_date = start_time.date()
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        start_ts = datetime.timestamp(start_time)

        diff = end_time - start_time
        days, seconds = diff.days, diff.seconds
        total_hour = days * 24 + seconds / 3600
        week_day = calendar.day_name[start_time.weekday()]

        # Check Job is exist or not
        job_query = """SELECT job_id, wage from {}_job WHERE job_name = '{}' AND status = '{}'""".format(user_id, job, 'active')
        cursor.execute(job_query)
        job_result = cursor.fetchall()
        connection.commit()
        
        if job_result is None:
            return {
                'msg': 'There is no job as {job}'
            }

        else:
            # Check shift exist or not
            job_id = job_result[0][0]
            shift_query = """SELECT * FROM {}_shift WHERE time_timestamp = {} AND job_id = {}""".format(user_id, previous_start_ts, job_id)
            cursor.execute(shift_query)
            shift_result = cursor.fetchall()
            connection.commit()

            if shift_result is None:
                return {
                    'msg': 'There is no shift on these time'
                }
            
            else:
                # Check is any other shift is therre in given time
                check_shift  = """
                        SELECT job_id, shift_day, shift_date, shift_start_time, shift_end_time, time_timestamp, total_hours
                        FROM {}_shift 
                        WHERE shift_date = '{}'
                    """.format(user_id, shift_date)
                cursor.execute(check_shift)
                check_result = cursor.fetchall()
                connection.commit()
                count = 0

                if check_result is None:
                    return 'No shift'
                
                else:
                    length = len(check_result)
                    for i in range(0, length):
                        check_start_time = check_result[i][3]
                        check_end_time = check_result[i][4]
                        
                        if (check_start_time <= start_time and check_end_time >= start_time) or (check_start_time <= end_time and check_end_time >= end_time) or (start_time <= check_start_time and end_time >= check_start_time) or (start_time <= check_end_time and end_time >= check_end_time):
                            count = count + 1
                    
                    # Update shift
                    if count == 0:
                        total_pay = total_hour*job_result[0][1]
                        shift_id = shift_result[0][0]
                        
                        update_query = """
                                        UPDATE {}_shift 
                                        SET job_id = {}, shift_day = '{}', shift_start_time = '{}', shift_end_time = '{}', total_hours = {}, pay = {}
                                        WHERE shift_id = {} AND time_timestamp = {}
                                        """.format(user_id, job_id, week_day, start_time, end_time, total_hour, total_pay, shift_id, start_ts)
                        cursor.execute(update_query)
                        connection.commit()

                        update_query = """
                                        UPDATE {}_shift 
                                        SET time_timestamp = {}
                                        WHERE shift_id = {}
                                        """.format(user_id, start_ts, shift_id)
                        cursor.execute(update_query)
                        connection.commit()

                        return {
                            'msg': 'Shifte added!'
                        }
                        
                    else:
                        return {
                            'msg': 'You already have shift on this time'
                        }
        
    except Exception as e:
        return f"Error: {str(e)}"
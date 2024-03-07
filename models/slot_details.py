from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
from datetime import datetime
from PIL import Image
import base64
from io import BytesIO
import json

# Simulated async function 
def addCarNumberApi(data):
    try:
        car_number = data['car_number']
        slot = data['slot_id']

        entry_time = datetime.now()

        # Insert data into database
        insert_query = "INSERT INTO `car_holder`(`slot_id`, `car_number`, `entry_time`, `total_pay`) VALUES (%s, %s, %s, %s)"
        insert_data = (
            slot,
            car_number,
            entry_time,
            0
        )
        cursor.execute(insert_query, insert_data)
        connection.commit()

        # Add into slot table
        datatable = "slot_"+slot
        insert_slot_query = "INSERT INTO `slot_{}`(`car_number`, `entry_time`, `total_payment`) VALUES (%s, %s, %s)".format(slot)
        insert_slot_data = (
            car_number, 
            entry_time, 
            0
        )
        cursor.execute(insert_slot_query, insert_slot_data)
        connection.commit()
        
        # Update status of slot
        update_query = "UPDATE  slot_status  SET  Available ='Unavailable' WHERE  slot_id = {}".format(slot)
        update_data = (slot)
        cursor.execute(update_query)
        connection.commit()

        cursor.close()
        connection.close()
        return "Isert sucessfuly"
    except Exception as err:
        return err
    
def exitCarProcessApi(data):
    try:
        car_number = data['car_number']
        slot = data['slot_id']

        exit_time = datetime.now()

        # Get Data
        select_query = "SELECT slot_id, entry_time, exit_time FROM car_holder WHERE car_number = %s AND slot_id = %s"
        select_data = (car_number, slot)
        cursor.execute(select_query, select_data)
        select_query_result = cursor.fetchone()
        
        different = exit_time - select_query_result[1]
        total_hours = int(different.total_seconds() /3600)
        total_pay = total_hours * 2.50
        tax = (total_pay *13)/100
        total_pay_tx = total_pay + tax

        # Insert data into database
        insert_query = "UPDATE `car_holder` SET `exit_time`= %s,`total_time`=%s,`total_pay`=%s WHERE `car_number` = %s AND exit_time IS NULL"
        insert_data = (
            exit_time,
            total_hours,
            total_pay_tx,
            car_number
        )
        cursor.execute(insert_query, insert_data)
        connection.commit()

        # Update into slot datatable
        slot_table_update = "UPDATE `slot_{}` SET `exit_time`= %s,`total_time`=%s,`total_payment`=%s WHERE `car_number` = %s AND exit_time IS NULL".format(slot)
        slot_table_update_data = (
            exit_time,
            total_hours,
            total_pay_tx,
            car_number
        )
        cursor.execute(slot_table_update, slot_table_update_data)
        connection.commit()

        # Update the status of the slot
        status_update_query = "UPDATE `slot_status` SET `Available`= 'Available' WHERE slot_id = %s"
        status_update_data = (slot, )
        cursor.execute(status_update_query, status_update_data)
        connection.commit()

        return {
            'data': "Thank you for choosing parking"
        }
    except Exception as err:
        return err
from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
from datetime import datetime
from PIL import Image
import base64
from io import BytesIO
import json

# Simulated async function 
def carParkApi(data):
    current_time = datetime.now()
    print(current_time)
    try: 
        cursor.execute("SELECT * FROM slot_status")
        results = cursor.fetchall()
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    return {'data': results}
        
def checkAvailableSlotApi():
    try:
        select_query = "SELECT slot_status.slot_id, slot_status.mall_slot_number, slot_details.code_name, slot_details.qr_code_image FROM slot_status LEFT JOIN slot_details ON slot_status.slot_id = slot_details.slot_id WHERE slot_details.status = 'active' AND slot_status.Available = 'Available' limit 1"
        cursor.execute(select_query)
        result = cursor.fetchone()
        cursor.close()
        connection.close()
 
        if result:
            slot_id, mall_slot_code, code_name, image_data = result
            img_bytesio = BytesIO(image_data)

            # update_status_query = "UPDATE `slot_status` SET `Available`='Unavailable' WHERE `slot_id`=%s;"
            # update_status_data = (slot_id)

            # cursor.execute(update_status_query, update_status_data)
            # connection.close()

            return {
                 'code_data' : code_name,
                 'img_data' : base64.b64encode(image_data).decode('utf-8'),
                 'slot_id': slot_id,
                 'mall_slot_code' : mall_slot_code
            }
        
        else:
            return "Image not found:"
            
    except Exception as err:
            return err
        
    

    

import mysql.connector
from mysql.connector import Error


# Replace these values with your MySQL server information
config = {
    'user': 'root',
    'password': 'Jainin@0511',
    'host': 'localhost',
    'database': 'money_handle'
}

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(buffered=True)
    print(cursor)
    print("Connected success")
    
except Error as err:
    print(f"Error: {err}")


# Create a cursor object for executing SQL queries




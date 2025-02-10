import mysql.connector
from database.config import db_config

def insert(eID, name, department):
    connection = None
    cursor = None
    try: 
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = "INSERT INTO employees(eID, name, department) VALUES (%s, %s, %s)"
        data = (eID, name, department)

        cursor.execute(insert_query, data)
        connection.commit()
        print("Database has been updated")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

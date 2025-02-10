import mysql.connector
from database.config import db_config

def read():
    try: 
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT * FROM employees"
        cursor.execute(query)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Display the rows
        for row in rows:
            print(row)

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
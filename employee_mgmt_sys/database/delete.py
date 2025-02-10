import mysql.connector
from database.config import db_config

def delete(eid):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "DELETE FROM employees WHERE eID = %s"
        cursor.execute(query, (eid,))
        connection.commit()  # Commit the transaction

        print(f"Record with eID {eid} deleted successfully")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

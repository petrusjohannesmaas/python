import sqlite3

def clear_daily_notes():
    # Connect to the database
    conn = sqlite3.connect('journal.db')
    cursor = conn.cursor()

    # SQL query to delete all records from the daily_notes table
    sql = "DELETE FROM daily_notes"

    try:
        # Execute the query
        cursor.execute(sql)
        # Commit the changes
        conn.commit()
        print("All records cleared from the daily_notes table.")
    except sqlite3.Error as err:
        print("Error:", err)
    finally:
        # Close the connection
        conn.close()

# Call the function
clear_daily_notes()

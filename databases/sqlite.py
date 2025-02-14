import sqlite3
from datetime import datetime

# Connect to db
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

print("Connected to the database.")

# Insert data
sql = """INSERT INTO trades (valid, bias, notes, traded, gain_in_pips, loss_in_pips, mood, date) 
         VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
data = (False, 'Neutral', 'Another note', False, 0, 0, 5, datetime.now().date())
try:
    cursor.execute(sql, data)
    conn.commit()
    print("Inserted a row into the database.")
except sqlite3.Error as err:
    print("Error:", err)

# Update data
sql = "UPDATE trades SET gain_in_pips = ? WHERE id = ?"
data = (35, 1)
try:
    cursor.execute(sql, data)
    conn.commit()
    print("Updated a row in the database.")
except sqlite3.Error as err:
    print("Error:", err)

# Delete data
sql = "DELETE FROM trades WHERE id = ?"
data = (4,)
try:
    cursor.execute(sql, data)
    conn.commit()
    print("Deleted a row from the database.")
except sqlite3.Error as err:
    print("Error:", err)

# Clear table
sql = "DELETE FROM trades"
try:
    cursor.execute(sql)
    conn.commit()
    print("Truncated the table.")
except sqlite3.Error as err:
    print("Error:", err)

# Read data
sql = "SELECT * FROM trades"
try:
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("No rows in the database.")
    else:
        print("Read the following rows from the database:")
        for row in rows:
            print(row)
except sqlite3.Error as err:
    print("Error:", err)

# Close the connection
conn.close()

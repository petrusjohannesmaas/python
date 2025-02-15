import sqlite3

def read_all_records():
    conn = sqlite3.connect('journal.db')
    cursor = conn.cursor()

    # Fetch all records from daily_notes
    cursor.execute("SELECT * FROM daily_notes")
    daily_notes_records = cursor.fetchall()

    # Fetch all records from trades
    cursor.execute("SELECT * FROM trades")
    trades_records = cursor.fetchall()

    conn.close()

    return {
        "daily_notes": daily_notes_records,
        "trades": trades_records
    }

# Call the function and print the results
records = read_all_records()

# Print daily notes records
print("Daily Notes Records:")
for record in records["daily_notes"]:
    print(record)

# Print trades records
print("\nTrades Records:")
for record in records["trades"]:
    print(record)

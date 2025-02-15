import sqlite3

def initialize_db():
    conn = sqlite3.connect('journal.db')
    cursor = conn.cursor()
    
    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS daily_notes")
    cursor.execute("DROP TABLE IF EXISTS trades")
    
    # Create daily_notes table
    cursor.execute("""
        CREATE TABLE daily_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL UNIQUE,
            notes TEXT
        )
    """)
    
    # Create trades table
    cursor.execute("""
        CREATE TABLE trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            timeslot INTEGER NOT NULL,
            valid BOOLEAN NOT NULL,
            traded BOOLEAN NOT NULL,
            prayed BOOLEAN NOT NULL,
            pips INTEGER,
            bias TEXT,
            FOREIGN KEY (date) REFERENCES daily_notes (date)
        )
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

# Call the function to initialize the database
initialize_db()

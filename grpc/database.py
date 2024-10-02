import sqlite3


class Database:
    def __init__(self, db_name="crud.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with self.get_connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )
            """
            )

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def insert_item(self, name):
        with self.get_connection() as conn:
            cursor = conn.execute("INSERT INTO items (name) VALUES (?)", (name,))
            return cursor.lastrowid

    def get_item(self, item_id):
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,))
            return cursor.fetchone()

    def update_item(self, item_id, name):
        with self.get_connection() as conn:
            conn.execute("UPDATE items SET name = ? WHERE id = ?", (name, item_id))

    def delete_item(self, item_id):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM items WHERE id = ?", (item_id,))

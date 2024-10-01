def initialize_database(self):
    cursor = self.connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS employees (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        department TEXT NOT NULL,
                        position TEXT NOT NULL,
                        salary REAL NOT NULL)"""
    )
    self.connection.commit()

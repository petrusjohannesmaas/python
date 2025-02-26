import os
from sqlalchemy import create_engine, text
import pandas as pd

# Database connection settings (Replace with your actual database settings)
db_settings = {
    "user": "your_db_user",
    "password": "your_db_password",
    "host": "your_db_host",
    "port": 3306,
    "database": "your_db_name",
}

# Create a database engine
engine = create_engine(
    f"mysql+pymysql://{db_settings['user']}:{db_settings['password']}@{db_settings['host']}:{db_settings['port']}/{db_settings['database']}"
)

def export_to_excel(table_name, output_file):
    # SQL query to fetch all data from the table
    query = f"SELECT * FROM {table_name}"
    
    # Execute the query and fetch data
    with engine.connect() as connection:
        result = connection.execute(text(query))
        data = result.fetchall()
    
    # Convert query result to a pandas DataFrame
    df = pd.DataFrame(data, columns=result.keys())
    
    # Save DataFrame to Excel file
    df.to_excel(output_file, index=False)
    print(f"Data exported to {output_file}")

# Example usage
if __name__ == "__main__":
    export_to_excel("example_table", "output.xlsx")

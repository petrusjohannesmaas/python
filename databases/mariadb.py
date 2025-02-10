import mysql.connector

# Database configuration
db_config = {
    'host': '172.17.0.2',
    'user': 'root',
    'password': 'employer123',
    'database': 'employee_mgmt_sys',
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

# Create a connection
try:
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to MariaDB")

except mysql.connector.Error as e:
    print(f"Error: {e}")
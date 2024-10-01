from flask import Flask, request, jsonify
import sqlite3
import threading

app = Flask(__name__)


# Singleton Database Connection Class
class Database:
    _instance = None
    _lock = threading.Lock()  # For thread safety

    def __new__(cls, db_file="employees.db"):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Database, cls).__new__(cls)
                    cls._instance.connection = sqlite3.connect(
                        db_file, check_same_thread=False
                    )
                    cls._instance.connection.row_factory = (
                        sqlite3.Row
                    )  # To return rows as dictionaries
        return cls._instance

    def get_connection(self):
        return self.connection


# Initialize the Singleton Database instance
db_instance = Database()


# Create a route to add a new employee (CREATE)
@app.route("/employees", methods=["POST"])
def create_employee():
    data = request.json
    name = data.get("name")
    department = data.get("department")
    position = data.get("position")
    salary = data.get("salary")

    conn = db_instance.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO employees (name, department, position, salary)
                      VALUES (?, ?, ?, ?)""",
        (name, department, position, salary),
    )
    conn.commit()

    return jsonify({"message": "Employee created successfully"}), 201


# Create a route to retrieve all employees (READ)
@app.route("/employees", methods=["GET"])
def get_employees():
    conn = db_instance.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    # Convert the SQLite Row objects to dictionaries
    employee_list = [dict(row) for row in employees]

    return jsonify(employee_list), 200


# Create a route to retrieve a single employee by ID (READ)
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    conn = db_instance.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
    employee = cursor.fetchone()

    if employee:
        return jsonify(dict(employee)), 200
    else:
        return jsonify({"message": "Employee not found"}), 404


# Create a route to update an employee's details (UPDATE)
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.json
    name = data.get("name")
    department = data.get("department")
    position = data.get("position")
    salary = data.get("salary")

    conn = db_instance.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE employees SET name = ?, department = ?, position = ?, salary = ?
                      WHERE id = ?""",
        (name, department, position, salary, employee_id),
    )
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"message": "Employee not found"}), 404
    else:
        return jsonify({"message": "Employee updated successfully"}), 200


# Create a route to delete an employee (DELETE)
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    conn = db_instance.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"message": "Employee not found"}), 404
    else:
        return jsonify({"message": "Employee deleted successfully"}), 200


# Main application entry point
if __name__ == "__main__":
    app.run(debug=True)

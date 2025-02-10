from flask import Flask, request, render_template
from database.insert import insert
from database.read import read
from database.delete import delete

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert_employee():
    eID = request.form['eID']
    name = request.form['name']
    department = request.form['department']

    insert(eID, name, department)
    return "Employee inserted successfully"

@app.route('/read', methods=['GET'])
def read_employees():
    read()
    return "Read attempted."

@app.route('/delete', methods=['POST'])
def remove_employee():
    eID = request.form['eID']
    delete(eID)  # Pass the eID to the delete function
    return "Employee removed successfully"

if __name__ == '__main__': 
    app.run()

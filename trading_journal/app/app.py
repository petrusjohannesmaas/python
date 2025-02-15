import sqlite3
from datetime import date
from flask import Flask, request, jsonify, render_template, make_response

app = Flask(__name__)

# Connect to db
def connection_string():
    conn = sqlite3.connect('journal.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/submit_report', methods=['POST'])
def submit_report():
    today = date.today()
    conn = connection_string()
    cursor = conn.cursor()

    for i in range(1, 7):
        valid = request.form.get(f'valid_{i}') == 'on'
        traded = request.form.get(f'traded_{i}') == 'on'
        prayed = request.form.get(f'prayed_{i}') == 'on'
        pips = request.form.get(f'pips_{i}')
        bias = request.form.get(f'bias_{i}')

        sql_insert = """INSERT INTO trades (date, timeslot, valid, traded, prayed, pips, bias) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)"""
        data_insert = (today, i, valid, traded, prayed, pips, bias)
        try:
            cursor.execute(sql_insert, data_insert)
            conn.commit()
        except sqlite3.Error as err:
            return jsonify({"message": f"Error: {err}"}), 500

    conn.close()
    return jsonify({"message": "Inserted 6 rows into the database."}), 200

@app.route('/update', methods=['POST'])
def update_notes():
    notes = request.form['notes']
    today = date.today()
    conn = connection_string()
    cursor = conn.cursor()

    # Check if there is a record for today
    cursor.execute("SELECT COUNT(*) FROM daily_notes WHERE date = ?", (today,))
    count = cursor.fetchone()[0]

    if count == 0:
        # No record for today, insert a new one
        sql_insert = "INSERT INTO daily_notes (date, notes) VALUES (?, ?)"
        data_insert = (today, notes)
        try:
            cursor.execute(sql_insert, data_insert)
            conn.commit()
            message = "Inserted a row into the database."
        except sqlite3.Error as err:
            message = f"Error: {err}"
    else:
        # Record for today exists, update the notes
        sql_update = "UPDATE daily_notes SET notes = ? WHERE date = ?"
        data_update = (notes, today)
        try:
            cursor.execute(sql_update, data_update)
            conn.commit()
            return render_template('success.html', today=today)
        except sqlite3.Error as err:
            message = f"Error: {err}"

    conn.close()
    return jsonify({"message": message}), 200

@app.route('/', methods=['GET'])
def index():
    empty = "There are no notes for today."
    conn = connection_string()
    cursor = conn.cursor()
    today = date.today()
    cursor.execute("SELECT notes FROM daily_notes WHERE date = ?", (today,))
    row = cursor.fetchone()
    conn.close()

    note = row['notes'] if row else empty
    modal_note = row['notes'] if row else ""
    resp = make_response(render_template('index.html', note=note, modal_note=modal_note, date=today))
    # Clear any cookies set previously
    resp.set_cookie('note', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)

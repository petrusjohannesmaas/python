from flask import Flask, render_template, redirect, request, session, url_for, jsonify
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)

users = {
    "Pieter": generate_password_hash(os.getenv("Pieter_PASSWORD")),
    "Tuliza": generate_password_hash(os.getenv("Tuliza_PASSWORD")),
}


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and check_password_hash(users[username], password):
            session["username"] = username
            print(f"New login: {username} has logged in")
            return redirect(url_for("index"))
        else:
            return jsonify({"message": "Invalid credentials!"}), 401
    return render_template("login.html")


@app.route("/admin")
def admin():
    administrators = ["Pieter", "Tuliza"]
    if session["username"] in administrators:
        return render_template("admin.html", username=session["username"])
    else:
        return render_template("unauthorized.html"), 401


if __name__ == "__main__":
    app.run(debug=True, port=5050)

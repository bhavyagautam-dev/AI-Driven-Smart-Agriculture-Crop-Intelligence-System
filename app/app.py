from flask import Flask, render_template, request, redirect, session, jsonify
import joblib
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import serial
import threading
import time

app = Flask(__name__)
app.secret_key = "secret123"

# ===== MODEL LOAD =====
model = joblib.load("models/crop_model.pkl")

# ===== GLOBAL SENSOR DATA =====
sensor_data = {
    "soil": 0,
    "temp": 0,
    "humidity": 0
}

# ===== SERIAL CONNECTION =====
ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

# ===== SERIAL READER THREAD =====
def read_serial():
    global sensor_data

    while True:
        try:
            line = ser.readline().decode().strip()

            if line:
                print("DATA FROM ARDUINO:", line)

                if "soil" in line:
                    parts = line.split(",")

                    for part in parts:
                        if "=" in part:
                            key, value = part.split("=")
                            key = key.strip()
                            value = value.strip()

                            if key == "soil":
                                sensor_data["soil"] = int(float(value))
                            elif key == "temp":
                                sensor_data["temp"] = float(value)
                            elif key == "humidity":
                                sensor_data["humidity"] = float(value)

        except Exception as e:
            print("ERROR:", e)

# ===== DATABASE INIT =====
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        nitrogen REAL,
        phosphorus REAL,
        potassium REAL,
        temp REAL,
        humidity REAL,
        ph REAL,
        rainfall REAL,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ===== HOME =====
@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")

    return render_template("index.html", user=session["user"])

# ===== SENSOR DATA API =====
@app.route("/sensor-data")
def sensor_api():
    return jsonify(sensor_data)

# ===== PREDICT =====
@app.route("/predict", methods=["POST"])
def predict():

    if "user" not in session:
        return redirect("/login")

    nitrogen = float(request.form["nitrogen"])
    phosphorus = float(request.form["phosphorus"])
    potassium = float(request.form["potassium"])
    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    prediction = model.predict([[nitrogen, phosphorus, potassium, temp, humidity, ph, rainfall]])
    result = prediction[0]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history (username,nitrogen,phosphorus,potassium,temp,humidity,ph,rainfall,result)
    VALUES (?,?,?,?,?,?,?,?,?)
    """, (session["user"], nitrogen, phosphorus, potassium, temp, humidity, ph, rainfall, result))

    conn.commit()
    conn.close()

    return render_template("index.html", prediction=result, user=session["user"])

# ===== HISTORY =====
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history WHERE username=?", (session["user"],))
    data = cursor.fetchall()

    conn.close()

    return render_template("history.html", data=data)

# ===== REGISTER =====
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",
                           (username,password))

            conn.commit()
            conn.close()

            return redirect("/login")

        except:
            return "User already exists"

    return render_template("register.html")

# ===== LOGIN =====
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[0], password):
            session["user"] = username
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")

# ===== LOGOUT =====
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# ===== FORGOT PASSWORD =====
@app.route("/forgot", methods=["GET","POST"])
def forgot():

    if request.method == "POST":
        username = request.form["username"]
        new_password = generate_password_hash(request.form["password"])

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET password=? WHERE username=?",
                       (new_password, username))

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("forgot.html")

# ===== START =====
if __name__ == "__main__":
    t = threading.Thread(target=read_serial)
    t.daemon = True
    t.start()

    app.run(debug=False)
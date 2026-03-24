from flask import Flask, render_template, request, redirect, session
import sqlite3
import joblib
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

# Load ML model
model = joblib.load("models/crop_model.pkl")


# 🗄️ Create Database
def create_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # History table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        nitrogen REAL,
        phosphorus REAL,
        potassium REAL,
        temperature REAL,
        humidity REAL,
        ph REAL,
        rainfall REAL,
        prediction TEXT
    )
    """)

    conn.commit()
    conn.close()


create_db()


# 🔐 Home (Protected)
@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html", user=session["user"])


# 🌾 Prediction + Save History
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

    # 💾 Save history
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history 
    (username, nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall, prediction)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        session["user"],
        nitrogen, phosphorus, potassium,
        temp, humidity, ph, rainfall,
        prediction[0]
    ))

    conn.commit()
    conn.close()

    return render_template("index.html", prediction=prediction[0], user=session["user"])


# 🧑‍💻 Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username,password) VALUES (?,?)",
                (username, password)
            )
            conn.commit()
        except:
            return "User already exists!"

        conn.close()

        return redirect("/login")

    return render_template("register.html")


# 🔑 Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = username
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")


# 🚪 Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


# 📊 History Page
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


# 🌡️ Sensor API (dummy)
@app.route("/sensor-data")
def sensor_data():

    data = {
        "temperature": 25,
        "humidity": 60,
        "soil_moisture": 45
    }

    return data


# 🚀 Run
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("models/crop_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    nitrogen = float(request.form["nitrogen"])
    phosphorus = float(request.form["phosphorus"])
    potassium = float(request.form["potassium"])
    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    prediction = model.predict([[nitrogen, phosphorus, potassium, temp, humidity, ph, rainfall]])

    return render_template("index.html", prediction=prediction[0])
@app.route("/sensor-data")
def sensor_data():

    data = {
        "temperature":25,
        "humidity":60,
        "soil_moisture":45
    }

    return data

if __name__ == "__main__":
    app.run(debug=True)
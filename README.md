# 🌱 AI-Driven Smart Agriculture & Crop Intelligence System

## 📌 Overview
This project focuses on building an AI-driven smart agriculture system
to assist farmers in making data-driven decisions for better crop yield
and sustainable farming.

## 🚀 Features
- Crop recommendation using Machine Learning
- Crop disease detection
- Yield prediction
- Smart irrigation suggestions
- Data visualization dashboard

## 🧠 Technologies Used
- Python
- Machine Learning
- Pandas, NumPy, Scikit-learn
- Flask / Streamlit
- IoT (Future Scope)

## 📂 Project Structure
- dataset/ → Crop dataset used for training  
- src/ → Machine learning and logic scripts  
- iot/ → Sensor data simulation and IoT integration  
- models/ → Trained machine learning models  
- app/ → Streamlit dashboard application

## ▶️ How to Run
1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Run the dashboard

streamlit run app/app.py

## Hardware Components
- ESP32 / Arduino
- Soil Moisture Sensor
- DHT11 Temperature & Humidity Sensor
- Rain Sensor
- pH Sensor
- Relay Module
- Water Pump

## System Architecture
Sensors such as soil moisture, temperature, humidity, and pH sensors
collect environmental and soil data.

These sensors are connected to a microcontroller (ESP32 / Arduino)
which sends the data to the Python backend system.

The backend processes the sensor data using machine learning models
to recommend suitable crops and generate irrigation advice.

The results are displayed on a Streamlit dashboard where farmers
can monitor conditions and make better agricultural decisions.  

## ⭐ Note
This project is under active development and will be enhanced
with real-time data, IoT integration, and advanced AI models.

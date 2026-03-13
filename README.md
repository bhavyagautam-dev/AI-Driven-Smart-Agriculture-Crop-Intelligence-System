# 🌱 AI-Driven Smart Agriculture & Crop Intelligence System

## 📌 Overview

The **AI-Driven Smart Agriculture & Crop Intelligence System** is an intelligent farming assistant designed to help farmers make **data-driven decisions**.
The system combines **Machine Learning, Web Technologies, and IoT integration** to recommend suitable crops and provide smart agricultural insights.

This project uses a **Flask-based web dashboard** where users can input environmental parameters such as soil nutrients, temperature, humidity, pH, and rainfall to receive **AI-based crop recommendations**.

Future enhancements include **real-time IoT sensor integration** for automated monitoring and irrigation suggestions.

---

## 🚀 Features

* 🌾 **AI Crop Recommendation System**
* 📊 **Interactive Web Dashboard**
* 🧠 **Machine Learning Model (Random Forest)**
* 🌡️ **Environmental Data Input (NPK, Temperature, Humidity, pH, Rainfall)**
* 🔌 **IoT Sensor Data Integration (Future Scope)**
* 🌍 **Farmer Decision Support System**

---

## 🧠 Technologies Used

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* Joblib

### Frontend

* HTML
* CSS
* JavaScript (basic)

### Dataset

* Kaggle Crop Recommendation Dataset

### Hardware (Future Scope)

* Arduino / ESP32
* Soil Moisture Sensor
* DHT11 Temperature & Humidity Sensor
* Relay Module
* Water Pump

---

## 📂 Project Structure

```
AI-Driven-Smart-Agriculture-Crop-Intelligence-System

app/
   app.py
   templates/
       index.html
   static/
       style.css

dataset/
   crop_data.csv

models/
   crop_model.pkl

src/
   train_model.py
   test_model.py

README.md
requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/AI-Driven-Smart-Agriculture-Crop-Intelligence-System.git
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the ML Model

```
python src/train_model.py
```

### 4️⃣ Run the Flask Application

```
python app/app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 📊 System Architecture

```
Sensors (IoT)
     ↓
Arduino / ESP32
     ↓
Flask Backend
     ↓
Machine Learning Model
     ↓
Web Dashboard
```

---

## 📷 Dashboard Preview

The system includes a **modern web dashboard** where users can enter environmental data and receive crop recommendations powered by AI.

---

## 🔮 Future Enhancements

* Real-time IoT sensor integration
* Smart irrigation automation
* Crop disease detection using computer vision
* Data visualization dashboard
* Weather API integration

---
## 👨‍💻 Team Members

- **Bhavya Gautam** – Project Developer (AI & Backend)
- **Bhavya Gautam** – Research & Idea Support
- **Kushagra Sharma** – Presentation

---
## ⭐ Project Status

🚧 Under Active Development

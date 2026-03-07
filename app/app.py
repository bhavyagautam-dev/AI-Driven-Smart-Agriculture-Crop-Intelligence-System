import streamlit as st
from iot.sensor_simulation import get_sensor_data
from src.irrigation import irrigation_advice

st.title("Smart Agriculture IoT Dashboard")

data = get_sensor_data()

st.write("Sensor Data", data)

advice = irrigation_advice(data["soil_moisture"])

st.write("Irrigation Advice:", advice)

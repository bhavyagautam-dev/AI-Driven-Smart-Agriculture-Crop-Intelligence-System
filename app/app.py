import streamlit as st
from iot.sensor_simulation import get_sensor_data
from src.irrigation import irrigation_advice
from src.crop_prediction import recommend_crop

st.title("AI Smart Agriculture IoT System")

sensor_data = get_sensor_data()

st.write("Sensor Data", sensor_data)

crop = recommend_crop(
    90,40,40,
    sensor_data["temperature"],
    sensor_data["humidity"],
    sensor_data["ph"],
    120
)

st.write("Recommended Crop:", crop)

irrigation = irrigation_advice(sensor_data["soil_moisture"])

st.write("Irrigation Advice:", irrigation)

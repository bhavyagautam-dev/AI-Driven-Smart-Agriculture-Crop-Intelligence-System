import joblib

model = joblib.load("models/crop_model.pkl")

prediction = model.predict([[90,40,40,25,80,6.5,200]])

print("Recommended Crop:", prediction[0])
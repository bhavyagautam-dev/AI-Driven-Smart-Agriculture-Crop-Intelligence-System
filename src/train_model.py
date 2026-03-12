import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("dataset/crop_data.csv")

X = data[[
"Nitrogen",
"phosphorus",
"potassium",
"temperature",
"humidity",
"ph",
"rainfall"
]]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

# save model
joblib.dump(model, "models/crop_model.pkl")

print("Model trained and saved successfully!")
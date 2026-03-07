import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/crop_data.csv")

# Features and label
X = data.drop("label", axis=1)
y = data["label"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier()

# Train
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/crop_model.pkl")

print("Model trained and saved successfully!")

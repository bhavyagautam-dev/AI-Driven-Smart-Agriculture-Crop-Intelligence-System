import joblib

model = joblib.load("models/crop_model.pkl")

def recommend_crop(N,P,K,temp,humidity,ph,rainfall):

    data = [[N,P,K,temp,humidity,ph,rainfall]]

    prediction = model.predict(data)

    return prediction[0]

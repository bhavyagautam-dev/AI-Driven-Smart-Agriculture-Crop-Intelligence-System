def recommend_crop(temp, humidity):

    if temp > 25 and humidity > 60:
        return "Rice"

    elif temp > 20:
        return "Wheat"

    else:
        return "Maize"

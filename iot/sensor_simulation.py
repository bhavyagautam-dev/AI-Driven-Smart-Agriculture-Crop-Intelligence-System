import random

def get_sensor_data():

    data = {
        "soil_moisture": random.randint(20,80),
        "temperature": random.randint(18,35),
        "humidity": random.randint(40,90),
        "ph": round(random.uniform(5.5,7.5),2)
    }

    return data

if __name__ == "__main__":
    print(get_sensor_data())

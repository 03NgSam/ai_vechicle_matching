import pandas as pd
import numpy as np

np.random.seed(1)
n = 4000

data = {
    "origin_lat": np.random.uniform(12.9, 13.1, n),
    "origin_lon": np.random.uniform(77.5, 77.7, n),
    "dest_lat": np.random.uniform(12.9, 13.1, n),
    "dest_lon": np.random.uniform(77.5, 77.7, n),
    "hour": np.random.randint(0, 24, n),
    "vehicle_type": np.random.choice(["bike", "auto", "car"], n),
}

df = pd.DataFrame(data)

df["distance_km"] = np.random.uniform(1, 30, n)
traffic_factor = np.where((df["hour"] >= 8) & (df["hour"] <= 10), 1.5, 1.0)

df["duration_min"] = df["distance_km"] * np.random.uniform(2.5, 4.5) * traffic_factor
df["fare"] = df["distance_km"] * np.random.uniform(8, 14)

df.to_csv("data/rides.csv", index=False)
print("Dataset created")

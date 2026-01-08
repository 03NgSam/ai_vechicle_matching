from fastapi import FastAPI
import joblib
from pricing.surge import surge_multiplier

app = FastAPI(title="AI Vehicle Matching API")

# Load trained model
model = joblib.load("models/eta_model.pkl")

@app.post("/ride/quote")
def get_ride_quote(distance_km: float, hour: int):
    eta = model.predict([[distance_km, hour]])[0]
    surge = surge_multiplier(hour)
    cost = distance_km * 10 * surge

    return {
        "eta_minutes": round(eta, 2),
        "estimated_cost": round(cost, 2),
        "surge_multiplier": surge
    }

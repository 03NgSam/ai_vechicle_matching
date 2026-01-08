from fastapi import FastAPI
import joblib
from pricing.surge import surge_multiplier

def get_demand_level(hour):
    if 8 <= hour <= 10 or 17 <= hour <= 20:
        return "high"
    return "normal"

app = FastAPI(title="AI Vehicle Matching API")

# Load trained model
model = joblib.load("models/eta_model.pkl")

@app.post("/ride/quote")
def get_ride_quote(distance_km: float, hour: int):
    eta = model.predict([[distance_km, hour]])[0]
    surge = surge_multiplier(hour)
    cost = distance_km * 10 * surge

    demand = get_demand_level(hour)

    if demand == "high":
        recommendation = "Peak-hour pricing applied due to high demand"
    else:
        recommendation = "Normal pricing due to balanced demand"

    return {
        "eta_minutes": round(eta, 2),
        "estimated_cost": round(cost, 2),
        "surge_multiplier": surge,
        "demand_level": demand,
        "recommendation": recommendation
    }

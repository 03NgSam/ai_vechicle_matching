from fastapi import FastAPI
import joblib
from pricing.surge import surge_multiplier

def get_demand_level(hour):
    if 8 <= hour <= 10 or 17 <= hour <= 20:
        return "high"
    return "normal"

def get_ride_category(cost, eta):
    if cost < 100:
        return "cheap"
    if eta < 30:
        return "fast"
    return "balanced"

app = FastAPI(title="AI Vehicle Matching API")

# Load trained model
model = joblib.load("models/eta_model.pkl")

@app.post("/ride/quote")
def get_ride_quote(distance_km: float, hour: int):
    eta = model.predict([[distance_km, hour]])[0]
    surge = surge_multiplier(hour)
    cost = distance_km * 10 * surge

    demand = get_demand_level(hour)
    category = get_ride_category(cost, eta)

    if demand == "high":
        recommendation = "High demand detected. Surge pricing applied."
    else:
        recommendation = "Normal demand. Standard pricing applied."

    return {
        "eta_minutes": round(eta, 2),
        "estimated_cost": round(cost, 2),
        "surge_multiplier": surge,
        "demand_level": demand,
        "ride_category": category,
        "recommendation": recommendation
    }

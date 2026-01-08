# AI Vehicle Matching & Dynamic Pricing System

## What is this project?

This project simulates how a ride-hailing application (such as Uber or Ola) decides:

* How long a ride will take (ETA)
* How much the ride should cost
* When surge pricing should be applied
* How this logic can be exposed through a simple API

The goal of the project is to demonstrate an **end-to-end AI workflow** in a clear, simple, and practical way.

---

## High-Level Flow (Easy to Understand)

1. Synthetic ride data is generated to simulate urban trips
2. A machine learning model predicts the Estimated Time of Arrival (ETA)
3. Demand is inferred based on time of day
4. Surge pricing is applied during high-demand periods
5. A FastAPI service returns ETA, cost, and explanations to the user

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* FastAPI
* Uvicorn

---

## Dataset Description

The dataset is synthetically generated to resemble real ride-hailing data.

Each record includes:

* Origin and destination latitude & longitude
* Hour of the day
* Trip distance (km)
* Trip duration (minutes)
* Fare amount
* Vehicle type

Peak-hour traffic effects are simulated to make the data more realistic.

---

## Machine Learning: ETA Prediction

* **Objective:** Predict trip duration (ETA)
* **Model:** Linear Regression
* **Features Used:**

  * Distance (km)
  * Hour of day
* **Target Variable:** Trip duration (minutes)
* **Evaluation Metric:** Mean Absolute Error (MAE)

The trained model is saved and reused during API inference.

---

## Demand Awareness

To simulate real-world demand patterns, the system uses a simple time-based demand logic:

* Peak hours (8–10 AM and 5–8 PM) → High demand
* Other hours → Normal demand

The detected demand level is returned in the API response along with a human-readable recommendation.

---

## Dynamic Pricing

* Surge pricing is applied during high-demand hours
* A surge multiplier increases the base fare during peak periods
* Pricing logic is rule-based and explainable

---

## API Usage

### Endpoint

`POST /ride/quote`

### Parameters

| Name        | Type  | Description                 |
| ----------- | ----- | --------------------------- |
| distance_km | float | Trip distance in kilometers |
| hour        | int   | Hour of the day (0–23)      |

### Sample Response

```json
{
  "eta_minutes": 48.7,
  "estimated_cost": 150,
  "surge_multiplier": 1.5,
  "demand_level": "high",
  "ride_category": "balanced",
  "recommendation": "High demand detected. Surge pricing applied."
}
```

---

## How to Run the Project

### 1. Generate Dataset

```bash
python data/generate_data.py
```

### 2. Train ETA Model

```bash
python models/train_eta.py
```

### 3. Start API Server

```bash
uvicorn api.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## Project Structure

```
ai-vehicle-matching/
├── data/        # Dataset generation
├── models/      # Model training and saved model
├── pricing/     # Surge pricing logic
├── ranking/     # Vehicle ranking logic
├── api/         # FastAPI service
└── README.md
```

---

## Why this project?

This project focuses on:

* Clear and readable code
* Practical machine learning usage
* Explainable logic
* Reproducibility
* Real-world relevance

The API response is designed to be user-friendly and easy to understand, reflecting real product behavior.

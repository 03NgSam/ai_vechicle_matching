import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

# Load data
df = pd.read_csv("data/rides.csv")

# Features & target
X = df[["distance_km", "hour"]]
y = df["duration_min"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)
print("MAE:", round(mae, 2))

# Save model
joblib.dump(model, "models/eta_model.pkl")

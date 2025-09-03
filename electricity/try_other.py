import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import numpy as np


# Load dataset
df = pd.read_csv("powerconsumption.csv")

# Features and target
X = df[["Temperature", "Humidity", "WindSpeed"]]
y = (df["PowerConsumption_Zone1"] + df["PowerConsumption_Zone2"] + df["PowerConsumption_Zone3"])/3



# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(
    n_estimators=200,     # number of trees
    max_depth=10,         # limit tree depth
    random_state=42
)
model.fit(X_train, y_train)


# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))

# Save model
joblib.dump(model, "power_model.pkl")
print("Model saved as power_model.pkl")

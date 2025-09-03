from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Define input schema
class InputData(BaseModel):
    Temperature: float
    Humidity: float
    WindSpeed: float

# Create FastAPI app
app = FastAPI(title="Electricity Consumption API")

# Load the trained model
model = joblib.load("power_model.pkl")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Electricity Consumption Prediction API"}

@app.post("/predict")
def predict(data: InputData):
    # Convert input to DataFrame
    input_df = pd.DataFrame([{
        "Temperature": data.Temperature,
        "Humidity": data.Humidity,
        "WindSpeed": data.WindSpeed
    }])
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    
    return {"forecast_kWh": round(float(prediction)/1000, 2)}

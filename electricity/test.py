import joblib
import pandas as pd

# load trained model
loaded_model = joblib.load("power_model.pkl")

# make a new prediction
sample = pd.DataFrame([[35, 76.9, 0.83]])
print("Prediction:", loaded_model.predict(sample))


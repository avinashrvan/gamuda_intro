import joblib
import pandas as pd
import numpy as np

# load trained model
loaded_model = joblib.load("power_model.pkl")



# minrow = np.array([ 3.247,11.34  ,0.05 ])
# maxrow = np.array([40.01 ,94.8  ,6.483])
# input = (np.array([12.57,47.9, 0.078])-minrow)/(maxrow-minrow)


# # make a new prediction
# sample = pd.DataFrame([input])
# result = loaded_model.predict(sample)* (44736.048650000004-12261.679913) + 12261.679913 


result = loaded_model.predict([[38, 88, 2]])
print("Prediction:", result)


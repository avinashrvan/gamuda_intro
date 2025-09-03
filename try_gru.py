import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
from keras import models
from keras import layers
from keras import layers
import matplotlib.pyplot as plt
from keras.optimizers import Adam

# Load the dataset
df = pd.read_excel("cleandata.xlsx")

# Extract the relevant columns
data = df[['Outdoor Temperature', 'Occupancy', 'Power Consumption']]
data.dropna(inplace=True)
data = data.drop(data.index[20967:21264])


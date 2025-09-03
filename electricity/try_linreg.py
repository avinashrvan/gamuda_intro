from sklearn import linear_model 
from numpy import asarray, absolute
from pandas import read_csv, read_excel
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold

url = 'cleandata.xlsx'
df = read_excel(url)
data = df[['Outdoor Temperature', 'Occupancy', 'Power Consumption']]
data.dropna(inplace=True)
data = data.drop(data.index[20967:21264])
data = data.values
# split dataset into input and output columns
X, y = data[:, :-1], data[:, -1]
regr = linear_model.LinearRegression()
regr.fit(X, y)



print(regr.predict([[11, 48]]))















# fit a final xgboost model on the housing dataset and make a prediction
from numpy import asarray, absolute
from pandas import read_csv, read_excel
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold


# load the dataset
url = 'cleandata.xlsx'
df = read_excel(url)
data = df[['Outdoor Temperature', 'Occupancy', 'Power Consumption']]
data.dropna(inplace=True)
data = data.drop(data.index[20967:21264])
data = data.values
# split dataset into input and output columns
X, y = data[:, :-1], data[:, -1]
# define model
model = XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=5)

cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
# evaluate model
scores = cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
# force scores to be positive
scores = absolute(scores)
print('Mean MAE: %.3f (%.3f)' % (scores.mean(), scores.std()) )
# # fit model
# model.fit(X, y)
# print(model.predict(asarray([10, 32])))

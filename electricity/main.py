
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.preprocessing import MinMaxScaler


df = pd.read_excel('cleandata.xlsx')
data = df[['Outdoor Temperature', 'Occupancy']]
data.dropna(inplace=True)
data = data.drop(data.index[20967:21264])
data = np.array(data.values)
np.save('data', data)







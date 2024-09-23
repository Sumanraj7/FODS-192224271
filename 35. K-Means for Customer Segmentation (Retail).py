from sklearn.cluster import KMeans
import pandas as pd

data = pd.read_csv('transaction_data.csv')
X = data[['total_amount', 'frequency']]

model = KMeans(n_clusters=3)
model.fit(X)

data['segment'] = model.labels_
print(data.head())

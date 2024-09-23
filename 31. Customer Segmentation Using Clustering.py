from sklearn.cluster import KMeans
import pandas as pd

data = pd.read_csv('customer_data.csv')
model = KMeans(n_clusters=3)
model.fit(data)

data['cluster'] = model.labels_
print(data.head())

from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('purchase_data.csv')
X = data[['total_spent', 'items_bought']]

model = KMeans(n_clusters=3)
model.fit(X)

data['cluster'] = model.labels_
plt.scatter(data['total_spent'], data['items_bought'], c=data['cluster'])
plt.show()

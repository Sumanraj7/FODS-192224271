from sklearn.cluster import KMeans

X_train = [[10, 500], [20, 600], [30, 700]]
model = KMeans(n_clusters=2)
model.fit(X_train)

new_customer = [[15, 550]]
print(model.predict(new_customer))

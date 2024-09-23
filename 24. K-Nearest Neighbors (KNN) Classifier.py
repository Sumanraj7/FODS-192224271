from sklearn.neighbors import KNeighborsClassifier

X_train = [[1, 2], [2, 3], [3, 4]]
y_train = [0, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

new_patient = [[2, 2]]
print(model.predict(new_patient))

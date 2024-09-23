from sklearn.tree import DecisionTreeRegressor

X_train = [[50000, 5], [30000, 3], [40000, 4]]
y_train = [15000, 12000, 13000]

model = DecisionTreeRegressor()
model.fit(X_train, y_train)

new_car = [[35000, 3]]
print(model.predict(new_car))

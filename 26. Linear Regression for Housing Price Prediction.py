from sklearn.linear_model import LinearRegression

X_train = [[1500, 3], [1800, 4], [1200, 2]]
y_train = [300000, 400000, 200000]

model = LinearRegression()
model.fit(X_train, y_train)

new_house = [[1600, 3]]
print(model.predict(new_house))

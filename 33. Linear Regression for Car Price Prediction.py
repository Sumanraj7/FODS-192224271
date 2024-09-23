from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv('car_data.csv')
X = data[['engine_size', 'horsepower']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

new_car = [[3.0, 200]]
print(model.predict(new_car))

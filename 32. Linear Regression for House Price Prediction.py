from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv('house_data.csv')
X = data[['size']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

new_house = [[2500]]
print(model.predict(new_house))

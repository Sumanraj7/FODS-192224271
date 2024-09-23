import pandas as pd

data = pd.read_csv('stock_data.csv')
variability = data['closing_price'].std()
print(variability)

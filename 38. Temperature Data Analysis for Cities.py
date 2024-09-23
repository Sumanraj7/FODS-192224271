import pandas as pd

data = pd.read_csv('temperature_data.csv')
mean_temp = data.groupby('city')['temperature'].mean()
std_temp = data.groupby('city')['temperature'].std()
range_temp = data.groupby('city')['temperature'].max() - data.groupby('city')['temperature'].min()

print(mean_temp, std_temp, range_temp)

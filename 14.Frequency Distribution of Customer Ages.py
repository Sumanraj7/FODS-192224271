import pandas as pd

data = {'Customer_Age': [23, 45, 23, 56, 45, 34, 23, 45, 56, 34, 34, 23, 56, 45, 23]}
df = pd.DataFrame(data)

age_distribution = df['Customer_Age'].value_counts()

print(age_distribution)

import pandas as pd

data = {'Likes': [10, 20, 20, 30, 10, 40, 50, 30, 20, 40, 50, 60, 20]}
df = pd.DataFrame(data)

like_distribution = df['Likes'].value_counts()

print(like_distribution)

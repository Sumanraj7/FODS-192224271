import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {'age': [25, 30, 35, 40], 'fat': [18.5, 22.1, 19.8, 21.4]}
df = pd.DataFrame(data)
print(df.mean(), df.median(), df.std())
sns.boxplot(df['age']), sns.boxplot(df['fat']), plt.show()
plt.scatter(df['age'], df['fat']), plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('soccer_players.csv')
top_goals = data.nlargest(5, 'goals')['name']
top_salaries = data.nlargest(5, 'salary')['name']
avg_age = data['age'].mean()
older_players = data[data['age'] > avg_age]['name']

plt.bar(data['position'], data['goals'])
plt.show()

print(top_goals, top_salaries, older_players)

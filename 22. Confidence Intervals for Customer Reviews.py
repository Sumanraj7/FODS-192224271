import pandas as pd
import scipy.stats as stats

data = pd.read_csv("customer_reviews.csv")
mean = data['rating'].mean()
conf_interval = stats.norm.interval(0.95, loc=mean, scale=stats.sem(data['rating']))
print(conf_interval)

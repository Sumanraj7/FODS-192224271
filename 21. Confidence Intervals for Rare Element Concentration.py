import numpy as np
import scipy.stats as stats
import pandas as pd

data = pd.read_csv("rare_elements.csv")
sample = data.sample(100).values.flatten()

mean = np.mean(sample)
std_err = stats.sem(sample)
conf_interval = stats.norm.interval(0.95, loc=mean, scale=std_err)
print(conf_interval)

import scipy.stats as stats
import matplotlib.pyplot as plt

placebo = [120, 118, 119, 117, 121]
treatment = [110, 111, 108, 112, 109]

t_stat, p_val = stats.ttest_ind(placebo, treatment)
print(p_val)

plt.boxplot([placebo, treatment])
plt.show()

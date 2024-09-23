import numpy as np
import scipy.stats as stats

drug_data = [10, 12, 8, 11, 9]
placebo_data = [5, 6, 7, 4, 6]

ci_drug = stats.t.interval(0.95, len(drug_data)-1, loc=np.mean(drug_data), scale=stats.sem(drug_data))
ci_placebo = stats.t.interval(0.95, len(placebo_data)-1, loc=np.mean(placebo_data), scale=stats.sem(placebo_data))

print(ci_drug, ci_placebo)

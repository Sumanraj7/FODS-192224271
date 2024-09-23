from scipy import stats

design_A = [0.12, 0.14, 0.15, 0.11, 0.13]
design_B = [0.18, 0.17, 0.19, 0.16, 0.18]

t_stat, p_val = stats.ttest_ind(design_A, design_B)
print(t_stat, p_val)

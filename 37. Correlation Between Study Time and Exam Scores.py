import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('student_data.csv')
plt.scatter(data['study_time'], data['exam_score'])
plt.show()

import numpy as np
student_scores = np.array([[75, 80, 90, 85], 
                           [88, 90, 78, 92],
                           [67, 76, 88, 82], 
                           [94, 85, 91, 89]])

subjects = ['Math', 'Science', 'English', 'History']

subject_averages = np.mean(student_scores, axis=0)

highest_avg_index = np.argmax(subject_averages)
highest_avg_subject = subjects[highest_avg_index]

print("Average scores for each subject:")
for subject, avg in zip(subjects, subject_averages):
    print(f"{subject}: {avg:.2f}")

print(f"\nHighest average subject: {highest_avg_subject} with an average score of {subject_averages[highest_avg_index]:.2f}")

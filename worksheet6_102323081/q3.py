import numpy as np
import matplotlib.pyplot as plt

# Data for the students
students = {
    'Arin': [85, 78, 92, 88],
    'Aditya': [79, 82, 74, 90],
    'Chirag': [90, 85, 89, 92],
    'Gurleen': [66, 75, 80, 78],
    'Kunal': [70, 68, 75, 85]
}

subjects = ['Math', 'Physics', 'Chemistry', 'English']

# Calculate total and average marks for each student
for student, marks in students.items():
    total = sum(marks)
    average = total / len(marks)
    print(f"{student}: Total = {total}, Average = {average:.2f}")

# Calculate subject-wise performance
subject_performance = np.array(list(students.values())).T
for i, subject in enumerate(subjects):
    avg_marks = np.mean(subject_performance[i])
    print(f"{subject}: Average Marks = {avg_marks:.2f}")

# Visualize the subject-wise performance
plt.figure(figsize=(10, 5))
for student, marks in students.items():
    plt.plot(subjects, marks, marker='o', label=student)
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Subject-wise Performance')
plt.legend()
plt.grid(True)
plt.show()

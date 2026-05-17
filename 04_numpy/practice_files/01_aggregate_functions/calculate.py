import numpy as np

marks = np.array([
    [80, 90, 70, 60],
    [55, 45, 88, 92],
    [70, 65, 75, 80]
])

total_marks = np.sum(marks)
avg_marks_per_student = np.mean(marks, axis=1)
max_marks_per_subject = np.max(marks, axis=0)
lowest_mark = np.min(marks)
std_dev_per_student = np.std(marks, axis=1)

print(f"Total marks: {total_marks}")
print(f"Average marks per student: {avg_marks_per_student}")
print(f"Maximum marks per subject: {max_marks_per_subject}")
print(f"Lowest mark in the array: {lowest_mark}")
print(f"Standard deviation per student: {std_dev_per_student}")

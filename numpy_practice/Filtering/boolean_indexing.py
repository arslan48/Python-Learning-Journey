import numpy as np

students = np.array([[85, 42, 90, 55],
                     [70, 88, 45, 92],
                     [30, 65, 78, 40]])
# 3 students, 4 subjects

passing_marks = students[students >= 50]
fail = students[students < 50]
mid_range_marks = students[(students > 50) & (students < 85)]
extreme_marks = students[(students > 90) | (students < 30)]

print(f"Pass student: {passing_marks}")
print(f" fail: {fail}")
print(f"Mid range marks: {mid_range_marks}")
print(f"Extreme marks: {extreme_marks}")


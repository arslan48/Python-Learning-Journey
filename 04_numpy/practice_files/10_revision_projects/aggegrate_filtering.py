import numpy as np

students = np.array([[80, 45, 90, 55],
                     [70, 88, 45, 92],
                     [30, 65, 78, 40]])

total = np.sum(students)
average = (np.mean(students,axis=1))
Maximum = np.max(students,axis=0)
std = np.std(students)

pass_students = students[students >= 50]
fail = students[students < 50]
fdf = students[(students > 40) & (students < 80)]
std_per_student = np.std(students, axis=1)
consistant = np.argmin(std_per_student)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Maximum: {Maximum}")
print(f"Std: {std}")
print(f"Pass students: {pass_students}")
print(f"Fail: {fail}")
print(f"FDF: {fdf}")
print(f"STD per student: {std_per_student}")
print(f"Consistant {consistant}")
import numpy as np

rng = np.random.default_rng()
students = rng.integers(low=0,high=101,size=5)
students[students <= 0] = np.mean(students[students > 0])
avg = np.mean(students)
max = np.max(students)
min = np.min(students)

pass_students = students[students >= 50]
np.save("student_data.npy", students)

print("Data saved!")

arr = np.load("student_data.npy")
print(arr)

print(f"Average: {avg:.2f}")
print(f"Max: {max}")
print(f"Min: {min}")
print(f"Pass students: {pass_students}")
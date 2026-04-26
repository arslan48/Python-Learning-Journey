import numpy as np

marks = np.array([80, 45, 90, 33, 70])
attendance = np.array([90, 75, 85, 60, 95])

np.savez("Student_data", marks,attendance)

loaded = np.load("Student_data.npz")
print(loaded["arr_0"])
print(loaded["arr_1"])

pass_students = marks[marks >= 50]
np.save("Pass_students",pass_students)

loaded1 = np.load("Pass_students.npy")

print(loaded1)
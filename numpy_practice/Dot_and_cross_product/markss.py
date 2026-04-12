import numpy as np
def student_rep(name,marks):
    average = np.mean(marks)
    return f"{name} average is {average}"
marks = np.array([23,44,35,35])
print(student_rep("Ali",marks))

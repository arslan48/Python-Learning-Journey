import numpy as np

scores = np.array([[45, 78, 90, 55],
                   [88, 92, 70, 65],
                   [30, 55, 48, 80],
                   [95, 60, 75, 85]])

bonus = scores + 5
double = scores * 2
minus = scores - 2
percentage = scores /100
first_two = scores[0:2] * 1.5

print(f"Bonus marks:\n{bonus}\n")
print(f"Doubled:\n{double}\n")
print(f"Penalty:\n{minus}\n")
print(f"Percentage:\n{percentage}\n")
print(f"First 2 students x1.5:\n{first_two}")

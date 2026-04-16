import numpy as np

marks = np.array([[50, 60, 70],
                  [80, 90, 100]])  # Shape: (2, 3)

bonus = np.array([[5],
                  [10]])           # Shape: (2, 1)
print(marks + bonus)

print(marks * 2)

extra = np.array([1,2,3])

print(f"Extra\n{marks + extra}\n")





import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60]])  # Shape: (2, 3)

b = np.array([[5, 5, 5]])    # Shape: (1, 3)

print(a * b)

print(a.shape)
print(b.shape)

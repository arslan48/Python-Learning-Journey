import numpy as np


stock = np.array([
    [10, 20, 30],
    [5, 15, 10]
]) # Shape (2, 3)


price_row = np.array([[5000, 8000, 2000]]) # Shape (1, 3)


result = stock @ price_row.T

print("Fixed with Transpose:")
print(result)
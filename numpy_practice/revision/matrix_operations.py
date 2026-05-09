import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

dot_prod = np.dot(A,B)
transpose = A.T
determinant = np.linalg.det(A)
Inverse = np.linalg.inv(A)
print(f"Dot product {dot_prod}\n")
print(f"Transpose {transpose}\n")
print(f"Determinant {determinant}\n")
print(f"Inverse {Inverse}")
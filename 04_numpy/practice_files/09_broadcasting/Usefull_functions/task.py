import numpy as np
arr = np.zeros((3,3))
arr1 = arr + np.ones((3,3))
result = arr1 * np.full((3,3),5)
minus = result - np.eye(3)
final_result = minus

print(final_result)
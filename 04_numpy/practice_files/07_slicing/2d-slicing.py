import numpy as np

arr2d = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

print(arr2d[0:3,-1])

print(arr2d[1, 2])
# arr2d[row, :] → select one row, all columns (horizontal)
print(arr2d[0, :])
# arr2d[:, col] → select all rows, one column (vertical)
print(arr2d[:, 0])


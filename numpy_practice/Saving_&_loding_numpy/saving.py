import numpy as np

array1 = np.array([
    [1,2,3,4],
    [4,5,6,7]
])

array2 = np.array([
    [1,3,2,4],
    [5,6,8,9]

])

np.savez_compressed("data2", array1,array2)
print("Arrays were Saved")
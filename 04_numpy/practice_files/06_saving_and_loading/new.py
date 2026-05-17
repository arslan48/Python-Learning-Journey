import numpy as np

loaded = np.load("data.npz")

array1 = loaded["arr_0"]
array2 = loaded["arr_1"]
print(array1)
print(array2)
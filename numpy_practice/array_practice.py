import numpy as np
array = np.array([5,10,15,20,25],dtype=np.int8)

print(array)
print(array.shape)
print(array.dtype)

array2 = np.array([
    [1,2,3],
    [4,5,6]
])

print(f"the array2 shape is {array2.shape}")
print(f"Sum of array2 is {array2.sum()}")
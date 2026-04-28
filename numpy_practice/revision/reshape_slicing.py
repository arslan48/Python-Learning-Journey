import numpy as np

array = np.array([1,3,3,4,5,3,8,9,0,4,7,2])
print(array.reshape(3,4))
print(array.reshape(-1,2))
print(array.shape)
# slicing

array2 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

print(f"Step\n{array2[::2]}")
print(f"Second and third row first two column \n{array2[2:,:2]} Slicing")
print(f"First and second row and first two column\n{array2[1:3,0:2]}")
print(f"Last column\n{array2[:,-1]}")

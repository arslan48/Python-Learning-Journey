import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])

print(data.reshape(6,-1).shape)

print(data.reshape(9,-1).shape)

print(data.reshape(4,-1).shape)

print(data.reshape(3,4,-1).shape)

print(data.reshape(2,-1,6).shape)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(f"arr reshape\n{arr.reshape(3,4)}")

print(f"3d arr reshape\n{arr.reshape(2,2,3)}")

print(f"inferred shape\n{arr.reshape(6,-1)}")
print(f"inferred shape\n{arr.reshape(-1,3)}")

arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(f"arr2\n{arr2.reshape(2,-1)}")

arr3 = np.array([10, 20, 30, 40, 50, 60])
reshp = arr3.reshape((3,2), order ='F')
print(reshp)

import numpy as np

arr = np.zeros((4,4))
arr[0::2,0::2] =1
arr[1::2,1::2] =1
print(arr)

# Flag Pattern

arr1 = np.zeros((4,4))
arr1[0:1] =1
arr1[2:3] =1
print(arr1)

# Diamond pattern

arr2 = np.zeros((5,5))
arr2[0:1,2:3] =1
arr2[1:2,1:4] =1
arr2[2:3] =1
arr2[3:4,1:4] =1
arr2[4:5,2:3] =1

print(arr2)
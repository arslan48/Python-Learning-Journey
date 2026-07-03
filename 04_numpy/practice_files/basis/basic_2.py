import numpy as np
arr = np.array([[2,4,6],[8,10,12]])
print(arr.mean(axis=1))

x = np.arange(1,10).reshape(3,3)
print(x.max(axis=0))

b = np.array([[1],[2],[3]])
a = np.array([1,2,3])
print(a + b)

arr1 = np.array([[10,20],[30,40],[50,60]])
print(arr1.sum(axis=0))
print(arr1.sum(axis=1))


import numpy as np

array = np.array([1,3,4,5,0], dtype= np.str_)
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")

# 3D array

arr_3d = np.array([[['A','B','C','D'],['E','F','G','H'],['I','J','K','L']],
                  [['M','N','O','P'],['Q','R','S','T'],['U','V','W','X']] 
                   ])
print(arr_3d.ndim)
print(arr_3d.shape)
print(arr_3d.size)

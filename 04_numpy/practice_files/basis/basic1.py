import numpy as np 
zero = np.zeros((2,4))
print(zero)
#sorting elements
arr = np.array([3,8,0,1,8,7,7,4])
sort = np .sort(arr)
print(sort)
#concatenate
a = np.array([1,4,5])
b = np.array([3,5,7])
concat = np.concatenate((a,b))
print(concat)
#concatenate 2D array 
x = np.array([
    [2,3,5],
    [4,5,7]
    ])

y = np.array([
    [6,3,5],
    [4,0,7]
    ])
conc = np.concatenate((x,y), axis=1)
print(conc)


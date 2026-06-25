import numpy as np
a = np.array([24,35,133,57])
print(a[3])
print(a.shape)
change = a[0]= 10
print(f"replace 24 with {change}")
slicing = a[0:3]
print(slicing)
b = np.array([
    [12,3,2,3],
    [23,4,5,8]
    ])
print(b.shape)
nd = b.ndim
print(nd)

c = np.array([
    [2,4,5,3],
    [4,4,5,7],
    [12,34,23,65]
    ])
#slic = c[:,2:4]
#print(slic)
slic = c[1:2,2:4]
print(slic)
last_row = c[2:3,3:4]
print(last_row)


import numpy as np 

array = np.array([1,2,3])
print(array +2)
print(array -5)
print(array **2)

#  Exercise

radii = np.array([2,3,7])
print(np.pi * radii ** 2)

array2 = np.array([2,5,7,8])
print(np.sqrt(array2))
print(np.square(array2))

# Comparasion

score1 = np.array([23,32,45,48])
score1[score1 < 30] = 0
print(score1)

num1 = np.array([2,3,4])
num2 = np.array([2,3,4])

print(num1 - num2)

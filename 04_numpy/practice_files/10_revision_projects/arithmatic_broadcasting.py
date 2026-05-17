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

# Broadcasting

number1 = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [12,45,88,45]
])

number2 = np.array([[10],
                    [1],
                    [3]])
print(number1.shape)
print(number2.shape)

print(number1 + number2)


import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
                    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

print(numbers.reshape(4,6))

print(numbers.reshape(6,4))

print(numbers.reshape(2,3,4))


print(numbers.reshape(2, -1))

print(numbers.reshape(-1, 6))

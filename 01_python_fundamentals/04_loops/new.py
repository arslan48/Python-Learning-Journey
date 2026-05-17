import numpy as np
arr = np.array([33,34,34,83,24])
for i in arr:
    print(np.sqrt(i))

# Numpy + For loop + condition

arr1 = np.array([10,15,10,30,34,50,40])
for  num in arr1:
    if num > 25:
        print(num)
    
# Find maximum Number

numbers = np.array([34, 67, 23, 89, 12, 78])
max_num = 0
for num in numbers:
    if num > max_num:
        max_num = num

print(f"Max number: {max_num}")
import numpy as np

radi = np.array([2,-2,0,-4])

print(np.pi * radi **2)

print(np.sqrt(np.abs(radi)))

print(np.abs(radi))

# Element-wise arithmetic

array1 = np.array([3,4,1])
array2 = np.array([2,4,7])

print(f"plus\n{array1 + array2}\n")
print(f"power\n{array1 ** array2}\n")
print(f"divide\n{array1 / array2}\n")

# Grocery store

quantity = np.array([3, 5, 2, 8, 1])

price = np.array([50, 30, 100, 20, 500])

total = quantity * price
charges = price + 10
m = quantity - price
added = quantity + price

print(f"Total bill:\n{total}\n")
print(f"Delivery charges:\n{charges}\n")
print(f"Quantity - Price:\n{m}\n")
print(f"Quantity + Price:\n{added}")

# comparison operators

score = np.array([80,90,89,48,89])

print(score[score>= 90])

print(score== 88)

# comparison operators

score = np.array([80,90,89,48,89])

print(score[score>= 80])

a = np.array([1,2,3,4])
b = np.array([3,4,3,4])

print(f"grater\n{a<b}\n")
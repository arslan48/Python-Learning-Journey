def introduce(name, age):
    return f"My name is {name}\nMy age is {age}"

print(introduce("Alice",32))

# sum

def add(c,d):
    return c+d
result = add(3,5)
print(result)
# Numpy

import numpy as np

def analyze(calu):
    total = np.sum(calu)
    average = np.mean(calu)
    return total, average

total, average = analyze(np.array([10,20,30,40]))

print(total)
print(average)
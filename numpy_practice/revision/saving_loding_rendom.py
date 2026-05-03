import numpy as np

array = np.array([
    [3,4,5],
    [5,9,8]
])

np.save("data",array)


array1 = np.array([1,3,3,5,6])
array2 = np.array([5,6,48,5])

np.savez("Data",array1,array2)

load = np.load("Data.npz")

print(load)

arr = load["arr_0"]
print(arr)

# Random numbers

rng = np.random.default_rng()
random = rng.integers(low=3,high=7,size=3)
print(random)

random2 = rng.uniform(low=2,high=3,size=3)
print(random2)



print(np.random.uniform(low=3,high=9,size=3))

import numpy as np
prices = np.array([200, 100, 300])

Quantity = np.array([
    [2, 3, 1],
    [1, 5, 0],
    [4, 0, 2]
])

result = Quantity @ prices

print(prices.shape)

print(result)
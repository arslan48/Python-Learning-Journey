import numpy as np
stock = np.array([
    [2, 5, 8],
    [4, 4, 8]
])

price = np.array([[43000, 48990, 57000]])

total = stock @ price.T

print(total)
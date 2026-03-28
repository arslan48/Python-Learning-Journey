import numpy as np
stock = np.array([
    [10, 20, 30],
    [5, 15, 10]
])

price = np.array([5000, 8000, 2000])

result = stock @ price
print("Total worth")
print(result)

I = np.eye(3)

multip = stock @ I

print(multip)

comp = (stock == multip).all()
print(comp)
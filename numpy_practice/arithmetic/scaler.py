import numpy as np

prices = np.array([100, 200, 300, 400, 500])

tex = prices *1.10

discount = prices[2:] -5

half = prices /2

print(f"Tex added:\n{tex}\n")
print(f"Discount on last 3:\n{discount}\n")
print(f"Half price:\n{half}")
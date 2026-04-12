import numpy as np

prices = np.array([100, 200, 300, 400, 500])

tex = prices * 0.10
discount = prices[1:] *0.5

print(tex)

print(discount)


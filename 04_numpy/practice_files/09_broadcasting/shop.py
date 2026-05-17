import numpy as np
shop = np.array([[100, 200, 300],
                 [400, 500, 600],
                 [700, 800, 900]]) 

discount = np.array([[10], [20], [30]])

disc = shop - discount
delivery = disc + 50

tax = np.array([5, 10, 15])

total = delivery - tax

print(total)
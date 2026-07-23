import matplotlib.pyplot as plt
import numpy as np

age = np.random.normal(loc=30, scale=5, size=100)
age = np.clip(age, 18, 50)

plt.hist(age, bins=10, color="skyblue", ec="black")

plt.show()

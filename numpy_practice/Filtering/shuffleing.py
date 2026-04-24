import numpy as np

rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

# Fruits

Fruits = np.array(["🍎","🍇","🍈","🍌","🍐"])
Fruit= rng.choice(Fruits, size=(3,3))
print(Fruit)
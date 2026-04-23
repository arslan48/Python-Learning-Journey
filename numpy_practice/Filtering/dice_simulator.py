import numpy as np
rng = np.random.default_rng()
dice1, dice2 = rng.integers(1, 7, size=2)
print(f"Dice 1: {dice1}, Dice 2: {dice2}")
rolls = rng.integers(1, 7, size=10) 
print(rolls)
print(len(rolls[rolls == 6]))
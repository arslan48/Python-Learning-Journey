import numpy as np

rng = np.random.default_rng(seed=42)


arr = rng.integers(low=1, high=102, size=(4,4)).astype(np.float64)


arr[arr < 12] = 0


mean_val = np.mean(arr[arr > 0])


arr[arr <= 0] = mean_val

print("Mean Value:", mean_val)
print(arr)
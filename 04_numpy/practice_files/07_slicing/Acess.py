import numpy as np
Access = np.array([
    [5, 2, 8],
    [1, 9, 4],
    [7, 3, 6]
])

Load = np.array([100, 200, 300])

total = Access @ Load

print(total)

I = np.eye(3)
print(f"prove\n{I @ Access}")
import numpy as np
arr = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9,  10, 11, 12],
                [13, 14, 15, 16]])

print(f"first two rows:\n{arr[0:2]}")

print(f"last row:\n{arr[-1:]}")

print(f"column 1 and 2 full rows:\n{arr[0:,1:3]}")

print(f"Row 1 and 2 column 0 and 1:\n{arr[1:3,0:2]}")

print()
import numpy as np
arr = np.array([[1,  2,  3,  4],
                [5,  6,  7,  8],
                [9,  10, 11, 12],
                [13, 14, 15, 16]])

print(f"first two rows:\n{arr[0:2]}")

print(f"last row:\n{arr[-1:]}")

print(f"column 1 and 2 full rows:\n{arr[:,1:3]}")

print(f"Row 1 and 2 column 0 and 1:\n{arr[1:3,0:2]}")

print(f"skip:\n{arr[::2]}")

arr1 = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120],
                [130, 140, 150, 160]])

print(f"last two rows:\n{arr1[2:4]}")

print(f"first two rows last two column{arr1[0:2,2:]}")

print(f"skip:\n{arr1[:,::2]}")
import numpy as np

# Create an array of 30 periods (school periods/classes)
periods = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                    21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

# Reshape into 5 rows and auto-calculate columns (6 columns)
print(periods.reshape(5,-1))

# Reshape into 3D array: 2 days, 5 weeks, 3 periods per week
print(periods.reshape(2,5,-1))

# Reshape into 6 rows and 5 columns per row
print(periods.reshape(-1,5))

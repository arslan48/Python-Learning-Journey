import numpy as np

prices = np.array([100, 102, 98, 105, 110, 108, 115, 120, 118, 125])
day1_3 = prices[:3]
day2_4 = prices[1:4]
day3_5 =np.mean(prices[2:5])
print(f"{day3_5:.2f}")

overall_avg = np.mean(prices)
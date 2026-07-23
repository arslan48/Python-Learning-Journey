import matplotlib.pyplot as plt
import numpy as np

marks = np.array([45, 67, 23, 89, 56, 78, 34, 90, 12, 65,
         54, 43, 76, 88, 92, 38, 47, 59, 61, 73,
         29, 81, 95, 40, 52, 68, 71, 85, 33, 58])

plt.hist(marks,bins=6,color="orange",ec="black")

plt.title("Real Student Marks Distribution",fontweight="bold",fontsize="20")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

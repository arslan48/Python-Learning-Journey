import matplotlib.pyplot as plt
import numpy as np

days=np.array(["Monday","Tuestday","Wednesday","Thursday","Friday"])
cup_sold=np.array([45,60,52,75,90])

plt.title("Weekly Coffee Sales")
plt.xlabel("Day of the Week")
plt.ylabel("Cups Sold")

plt.grid(axis="y",alpha=0.5)

bar=plt.bar(days,cup_sold,color="#3299a8")
plt.bar_label(bar)
plt.show()

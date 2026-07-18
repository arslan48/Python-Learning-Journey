import matplotlib.pyplot as plt
import numpy as np
x = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([27,34,21,17])
y3 = np.array([12,14,25,38])
line_style = dict(marker=".",markersize=8,linewidth=2)
plt.title("Class",fontsize=30,family="Arial",fontweight="bold",color="green")
plt.xlabel("Year",fontsize=16,family="Arial",color="#1856f2")
plt.ylabel("Students",fontsize=16,family="Arial",color="#1856f2")
plt.tick_params(axis="both",colors="#1856f2")

plt.plot(x,y1,**line_style)
plt.plot(x,y2,**line_style)
plt.plot(x,y3,**line_style)
plt.xticks(x)
plt.show()

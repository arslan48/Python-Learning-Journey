import matplotlib.pyplot as plt
import numpy as np 

x=np.array([2,4,5,3,5])
y=np.array([30,45,56,86,97])

plt.title(
	"Hi",
	color="green",
	fontsize=35,
	family="arial",
	fontweight="bold")

plt.grid(axis="both",linestyle="--",alpha=0.5)

plt.scatter(x,y)
plt.show()
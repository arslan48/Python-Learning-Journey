import matplotlib.pyplot as plt
import numpy as np

x=np.array([3,4,2,5,3])
y=np.array([4,6,3,1,6])

colors=["#dc8a78","#dd7878","#ea76cb","#8839ef","#d20f39"]

figure,axes = plt.subplots(2,2)

axes[0,0].bar(x,y,color="lightgreen")
axes[0,0].set_title("Bar Chart")

axes[0,1].plot(x,x*2,color="pink")
axes[0,1].set_title("Plot")

axes[1,0].scatter(x,y,color="purple")
axes[1,0].set_title("Scatter Plot")

axes[1,1].pie(
	x,
	labels=y,
	colors=colors,
	autopct="%1.1%%",
	explode=[0,0,0,0,0.1]
)
axes[1,1].set_title("Pie")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

activities = ["Sleep", "Study", "Phone/Social Media", "Coding", "Other"]
hours = np.array([7, 4, 3, 5, 5])

colors=["#dc8a78","#dd7878","#ea76cb","#8839ef","#d20f39"]

plt.title("My Daily Time Distribution",fontsize=20,family="arial",fontweight="bold")

plt.pie(
	hours,
	labels=activities,
	autopct="%1.1f%%",
	colors=colors,
	shadow=False,
	explode=[0.1,0,0,0,0]
)

plt.show()

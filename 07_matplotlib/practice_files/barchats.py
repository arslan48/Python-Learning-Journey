import matplotlib.pylab as plt
import numpy as np
foods = np.array(["Pizza", "Burger", "Fries", "Pasta", "Sandwich"])
rating =np.array([9, 8, 7, 8.5, 6])
plt.tick_params(axis="both",colors="#8839ef")

plt.bar(foods,rating,color="#8839ef",alpha=0.7)

#for horizental 
#plt.barh(foods,rating,color="#8839ef",alpha=0.7)

plt.title("Food ratings",fontsize=25,family="Georgia",color="#8839ef")
plt.xlabel("foods",fontsize=16,family="arial",color="#8839ef")
plt.ylabel("Rating",fontsize=16,family="arial",color="#8839ef")
plt.grid(axis="y",alpha=0.5,linestyle="dotted")

plt.show()

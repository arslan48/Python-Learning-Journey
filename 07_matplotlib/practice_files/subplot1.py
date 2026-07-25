import matplotlib.pyplot as plt
import numpy as np

x= np.array([2,4,2,5,3])
y= np.array([1,3,5,3,6])

figure,axes = plt.subplots(1,2) 

axes[0].plot(x,x*2,color="skyblue",linestyle="dotted")
axes[0].set_title("bar graph")
axes[0].grid(axis="both",alpha=0.3)

axes[1].pie(x,labels=y,autopct="%1.1f%%",explode=[0,0.1,0,0,0],shadow=False)

plt.show()

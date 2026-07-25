import matplotlib.pyplot as plt
import numpy as np

Months = np.array(["Jan","Feb","Mar","Apr","May"])
Sales = np.array([10,15,13,18,20])

subjects = np.array(["Python","C++","Java"])
students = np.array([25,18,15])

x = np.array([1,2,3,4,5])
y = np.array([2,4,5,4,6])

scores= np.random.normal(loc=80,scale=10,size=100)
scores=np.clip(scores,0,100)

figure,axes = plt.subplots(2,2)
axes[0,0].plot(Months,Sales,color="skyblue")
axes[0,0].set_title("Monthely Sales")

axes[0,1].bar(subjects,students,color="skyblue")
axes[0,1].set_title("Bar")

axes[1,0].scatter(x,y,color="skyblue",s=120)
axes[1,0].set_title("Scatter")

axes[1,1].hist(scores,color="skyblue",ec="black")
axes[1,1].set_title("Scores")

plt.show()

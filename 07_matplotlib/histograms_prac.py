import matplotlib.pyplot as plt
import numpy as np

score=np.random.normal(loc=50,scale=10,size=100)
score=np.clip(score,0,100)

plt.hist(score,color="pink",bins=10,ec="black")

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Histogram of Scores")

plt.grid(axis="y",alpha=0.3)
plt.show()

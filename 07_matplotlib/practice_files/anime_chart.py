import matplotlib.pylab as plt
import pandas as pd

anime_df = pd.read_csv("anime_full.csv")
x = anime_df["Title"]
y = anime_df["Rating"] 

plt.plot(x,y,color="purple",linewidth=2,marker="s")
plt.title("Anime Data")
plt.xlabel("Anime")
plt.ylabel("Rating")
plt.xticks(rotation= 45, ha="right")
plt.tight_layout()
plt.show()

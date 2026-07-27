import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("food.csv")

plt.bar(df["food"],df["rating"], color="#8839ef")

plt.title("Food Ratings from CSV",family="arial",fontweight="bold")
plt.xlabel("Food")
plt.ylabel("Rating")

plt.show()
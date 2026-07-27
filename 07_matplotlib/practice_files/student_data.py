import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student.csv")

fav_subjects=(df["favorite_subject"].value_counts(ascending=True))

plt.barh(fav_subjects.index,fav_subjects.values,color="lightgreen",ec="black")

plt.title("Favorite Subjects",fontweight="bold")

plt.show()

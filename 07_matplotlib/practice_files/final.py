import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("data.csv")

fig, axes = plt.subplots(1,2 , figsize=(14, 10))
fig.suptitle("Pokemon Dataset Visual Analysis", fontsize=16)

type1_counts = df["Type1"].value_counts().head(8)

axes[0].bar(type1_counts.index,type1_counts.values,color="skyblue",ec="black")
axes[0].tick_params(axis="both",rotation=45)

type2_counts = df["Type2"].value_counts(ascending=True)

axes[1].barh(type2_counts.index,type2_counts.values,color="pink",ec="black")

plt.show()

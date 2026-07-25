from typing import Any

import matplotlib.pylab as plt
import numpy as np

years = np.array([2023, 2024, 2025, 2026])
naruto = np.array([70, 65, 60, 58])
onepiece = np.array([80, 85, 90, 95])
aot = np.array([90, 88, 75, 70])

line_style: dict[str,Any] ={
	"marker":".",
	"markersize":10,
	"linewidth":2
}

plt.title("Anime Ratings",fontsize=22,family="arial",fontweight="bold",color="#8839ef")
plt.xlabel("Years",fontsize=12,family="arial",color="#8839ef")
plt.ylabel("Ratings",fontsize=12,family="arial",color="#8839ef")

plt.tick_params(axis="both",colors="#8839ef")

plt.plot(years, naruto,color="#fe640b",label="Naruto",**line_style)
plt.plot(years,onepiece,color="#8839ef",label="One piece",**line_style)
plt.plot(years,aot,color="#ea76cb",label="AOT",**line_style)

plt.grid(axis="both",linewidth=2,color="#7c7f93")

plt.legend()
plt.xticks(years)
plt.show()

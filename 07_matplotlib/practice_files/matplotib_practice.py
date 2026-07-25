from typing import Any

import matplotlib.pyplot as plt

x = [2023,2024,2024,2025,2026]
y1 = [25,30,45,60,0]
y2 = [10,24,13,39,10]
y3 = [15,20,25,30,35]

line_style: dict[str,Any] = {
	"marker":".",
    "markersize":30,
	"mfc":"#34ebb1",
    "mec":"#34ebb1",
    "linestyle":"solid",
	"linewidth":4,
}
plt.plot(x,y1,color="#c334eb",**line_style)
plt.plot(x,y2,color="#4287f5",**line_style)
plt.plot(x,y3,color="#9a75f0",**line_style)
plt.show()

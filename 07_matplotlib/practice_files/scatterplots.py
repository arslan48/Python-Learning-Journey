import matplotlib.pyplot as plt
import numpy as np

# Data
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
exam_score = np.array([50, 55, 65, 68, 75, 82, 88, 95])

study_hours2 = np.array([3, 1, 5, 6, 5, 8, 4, 3])
exam_score2 = np.array([60, 35, 69, 76, 95, 60, 88, 81])

# Scatter Plot
plt.scatter(
	study_hours,
	exam_score,
	color="#dd7878",
	alpha=0.5,
	s=200,
	label="Class A"
)

plt.scatter(
	study_hours2,
	exam_score2,
	color="#8839ef",
	alpha=0.5,
	s=200,
	label="Class B"
)

plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title(
	'Study Hours vs Exam Score',
	fontsize=20,
	family="arial",
	fontweight="bold"
)
plt.grid(
	axis="both",
	linestyle="--",
	alpha=0.3,
)

plt.legend()
plt.show()

import numpy as np

marks = np.array([45, 78, 62, 90, 38, 75, 88, 55])

total_marks = np.sum(marks)

class_average = np.mean(marks)

median_marks = np.median(marks)

highest_marks = np.max(marks)

lowest_marks = np.min(marks)

marks60 = marks[marks>60]


print(f"Total Marks:    {total_marks}")
print(f"Class Average:  {class_average}")
print(f"Median:         {median_marks}")
print(f"Highest:        {highest_marks}")
print(f"Lowest:         {lowest_marks}")
print(f"Above 60:       {len(marks60)} students")


import numpy as np

def get_average(mark):
    return np.mean(mark)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    else:
        return "F"

marks = np.array([55, 78, 92, 43, 67, 88])

average = get_average(marks)
grade = get_grade(average)

print(f"{average:.2f}")
print(f"Grade {grade}")
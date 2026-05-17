import numpy as np


marks = np.array([78, 85, 92, 45, 67, 88, 
                  73, 91, 56, 83, 69, 77])

def reshape_marks(marks):
    print(f"--Reshaped--")
    reshaped = marks.reshape(3,4)
    print(reshaped)

reshape_marks(marks)

def analyze_marks(marks):
    print(f"--analyze--")
    average = np.mean(marks)
    highest = np.max(marks)
    lowest = np.min(marks)
    above60 = len(marks[marks>60])

    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest:  {lowest}")
    print(f"Above 60: {above60} students")

analyze_marks(marks)


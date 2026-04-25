import numpy as np

rng = np.random.default_rng()
names = np.array(["Ali", "Sara", "Ahmed", "Hassan", "Maya"])
marks = rng.integers(0, 101, size=5)

passing = marks[marks >=40]
fail = marks[marks < 40]

highest = np.max(marks)
lowest = np.min(marks)
average = np.mean(marks)

print(f"Pass Students: {passing}")
print(f"Fail Student: {fail}")
print(f"Highest marks: {highest}")
print(f"loweset marks: {lowest}")
print(f"Average marks: {average}")
rng.shuffle(marks)
print(f"Shuffle: {marks}")
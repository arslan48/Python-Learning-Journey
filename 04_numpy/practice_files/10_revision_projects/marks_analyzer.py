import numpy as np

students = np.array([
    [12,80,89,45],
    [80,84,43,84],
    [76,23,45,92],
    [45,73,32,90]
])

subjects = np.array(["Maths","Physics","Chemistry","English"])

names = np.array(["Ali","Sara","Ahmed","John"])

average = np.mean(students,axis=1)
Total = (np.sum(students,axis=1))
pas = students[students > 33]
fail = students[students < 33]
best_avg = np.mean(students,axis=1)
best_student = names[np.argmax(average)]
stdd = np.std(students,axis=1)
consistent = np.argmin(stdd)
subject_high_marks = np.max(students,axis=0)


np.save("Student_data",students)

print(f"Average marks: {average}")
print(f"Total marks: {Total}")
print(f"Best student: {best_student}")
print(f"Most consistent student: {names[consistent]}")
print(f"Subject highest marks: {subject_high_marks}")
print(f"Passing marks: {pas}")
print(f"Failing marks: {fail}")
print("file saved!")
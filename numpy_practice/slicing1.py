import numpy as np

scores = np.array([
    [85, 90, 88], # Index 0
    [70, 75, 72], # Index 1
    [95, 92, 98], # Index 2
    [60, 65, 62]  # Index 3
])

sara_marks = scores[1,:]

print(sara_marks)

jan_marks = scores[:,0]

print(jan_marks)

zain_feb = scores[2,1]

print(zain_feb)

hina_march = scores[3,2]

print(hina_march)

ali_feb = scores[0,1]

print(ali_feb)
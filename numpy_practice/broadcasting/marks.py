import numpy as np

students = np.array([[50, 60, 70],
                     [80, 90, 100],
                     [40, 55, 65]])  # 3 students, 3 subjects

curve = np.array([[5, 10, 15]])  

result = (students + curve)/2

print(result)
print(curve.shape)
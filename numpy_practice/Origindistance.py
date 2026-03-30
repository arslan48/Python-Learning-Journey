import numpy as np

point = np.array([6,8]) 
dis = np.linalg.norm(point)

print(dis)

# Distance Between 2 Points

P1 = np.array([10, 15])
P2 = np.array([22, 20])

diss = np.linalg.norm(P1-P2)

print(diss)

# 3d distance

S1 = np.array([5,12,9])
S2 = np.array([8,14,11])
dis_3d = np.linalg.norm(S1-S2)
print(dis_3d)
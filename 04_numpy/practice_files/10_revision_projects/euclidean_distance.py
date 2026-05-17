import numpy as np
from numpy.linalg import norm

Point1 = np.array([1,2])
point2 = np.array([4,6])

distance = np.linalg.norm(Point1 -point2)
print(f"{distance}")

# Cosine_similarity

import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

cosine_sim = np.dot(A, B) / (norm(A) * norm(B))

print(f"{cosine_sim:.4f}")
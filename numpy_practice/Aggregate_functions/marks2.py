import numpy as np

alice = np.array([50, 70, 90])
bob  = np.array([70, 60, 90])

total_a = np.sum(alice)
total_b = np.sum(bob)
aver_a = np.mean(alice)
aver_b = np.mean(bob)
max_marks_a = np.max(alice, axis=0)
max_marks_b = np.max(bob, axis=0)
compare = alice > bob

print(f"Alice Total: {total_a}, Average: {aver_a}, Max: {max_marks_a}")
print(f"Bob Total: {total_b}, Average: {aver_b}, Max: {max_marks_b}")
print(f"Alice > Bob: {compare}")

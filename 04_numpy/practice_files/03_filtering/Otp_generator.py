import numpy as np

rng = np.random.default_rng()
otp = rng.integers(0,10,size=6)
print(''.join(map(str,otp)))
import numpy as np

ages = np.array([
    [22,45,34,23,23,34,12,34,14],
    [13,45,80,24,13,17,45,14,56]
])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages <= 60)]
even = ages[ages %2 == 0]
odd = ages[ages %2 != 0]
print(f"Teenagers: {teenagers}")
print(f"Adults: {adults}")
print(f"Even: {even}")
print(f"Odd: {odd}")

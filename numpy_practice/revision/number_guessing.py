import numpy as np
user = int(input("Enter the number:"))

rng = np.random.default_rng()

numbers = rng.integers(low=1, high=101,size=1)

if user == numbers[0]:
    print("Your guess is right")
elif user > numbers[0]:
    print("higher expectation")
else:
    print("wrong guess")

print(f"Correct number is {numbers}")

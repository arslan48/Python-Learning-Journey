import numpy as np

rng = np.random.default_rng()
celsius = np.round(rng.uniform(low=0, high=40,size=5),1)


fahrenheit = (celsius * 9 / 5) + 32
filtered = celsius[celsius > 30]
average_temperature = np.mean(celsius)

print(f"celsius: {celsius}")
print(f"fahrenheit: {fahrenheit}")
print(f"filtered: {filtered}")
print(f"average temperature: {average_temperature:.2f}")

rng.shuffle(celsius)  # shuffle values
print(f"Shuffled: {celsius}")
import numpy as np

rng = np.random.default_rng()
alice, bob, karlo, john, maya = rng.integers(1,101, size=5)
print(f"Alice random number: {alice}")
print(f"john random number: {john}")
print(f"karlo random number: {karlo}")
print(f"bob random number: {bob}")
print(f"maya random number: {maya}")

players = np.array([alice, bob, karlo, john, maya])
winner = np.max(players)
loser = np.min(players)
names = np.array(["Alice", "Bob", "Karlo", "John", "Maya"])

winner_name = names[np.argmax(players)] 
loser_name = names[np.argmin(players)]

print(f"Winner: {winner_name} with {winner}")
print(f"Loser: {loser_name} with {loser}")
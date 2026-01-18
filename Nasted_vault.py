vault = [("Gold", 500), ("Diamonds", 10), ("Silver", 1000)]
my_gems = vault[1]
print(f"My gems are {my_gems}")
Silverrr = list(vault[2])
Silverrr[1] = 1500
Silverrr = tuple(Silverrr)
print(f"My silver is {Silverrr}")
vault.append(("Platinum", 5))
total_items = vault[0][1] + vault[1][1] + vault[2][1] + vault[3][1]
  
print(f"updated vault: {vault}")
print(f"Total items in vault: {total_items}") 
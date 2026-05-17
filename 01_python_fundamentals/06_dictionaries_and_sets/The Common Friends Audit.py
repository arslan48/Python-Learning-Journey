zain_friends = {"Ali", "Khan", "Ahmed", "Sara", "Raza"}
ali_friends = {"Ahmed", "Sara", "Hamza", "Zoha"}
# Add function 

zain_friends.add("Bilal")

# Remove function 
zain_friends.discard("Raza")
print(zain_friends)

# Intersection
zain_friends.intersection((ali_friends))
print(f"Common Friends: {zain_friends}")

# Union

zain_and_ali_friends = zain_friends.union(ali_friends)
print(f"Zain and Ali Friends: {zain_and_ali_friends}")

# difference

only_zain_friends = zain_friends.difference(ali_friends)
print(f"Only Zain Friends: {only_zain_friends}")
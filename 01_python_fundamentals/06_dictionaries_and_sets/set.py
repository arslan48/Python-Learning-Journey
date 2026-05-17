guests = ["Zain", "Ali", "Khan", "Zain", "Ali"]
guests = set(guests)
print(guests)

guests.add("Ahmed")
print(guests)

guests.update(["Sara", "Raza"])
print(guests)


guests.discard("umer")
print(guests)

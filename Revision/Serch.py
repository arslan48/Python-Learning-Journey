fruits = ["Mango", "Banana", "Apple", "Grapes", "Orange"]
for fruit in fruits:
    print(f"Checking: {fruit}")
    if fruit == "Apple":
        pos = fruits.index(fruit)
        print(f"Found it at index {pos}")
        break
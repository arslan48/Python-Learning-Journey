# Dictionary containing fruit names and their prices
prices = {"apple": 100, "banana": 50, "orange": 80}


# Ask the user to enter a fruit name
fruit = input("Enter the fruit name: ")


# Check if the fruit is in the dictionary using .get()
# If found, return the price; otherwise, return "Fruit is not available"
check = prices.get(fruit, "Fruit is not available")


# Print the result (price or unavailability message)
print(check)



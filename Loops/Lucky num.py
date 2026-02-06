guess = 0
while guess != 4:
    guess = int(input("Enter the number:"))
    if guess != 4:
        print("Wrong! Try again:")
print(f" congratulations your guess is correct: {guess}") 
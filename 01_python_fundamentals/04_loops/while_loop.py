# basic
i = 1
while i <=10:
    print(i)
    i = i + 1

# user input 

total = 0
number = int(input("Enter the number: "))

while number != 0:
    total = total + number
    number = int(input("Enter number: "))
print(f"sum: {total}")

# count down from 10

e = 10
while e >= 1:
    print(e)
    e = e -1

# Guess the number 

numb = int(input("Enter the number: "))
secret = 7 
while numb != secret:
    print("Wrong! Try again.")
    numb = int(input("Enter the number: "))

print("Correct")

# Multiplication Table with While Loop

t = 1
table = int(input("Enter the number: "))
while t != 11:
    print(f"{table} x {t} = {t * table}")
    t = t + 1
    
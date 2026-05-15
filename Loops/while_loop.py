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

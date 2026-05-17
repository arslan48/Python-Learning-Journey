numbers = [10,20,30,40]
total = 0
for num in numbers:
    
    total= total +num
print(total)

for numer in range(1,11):
    print(f"numers {numer}")

# Even numbers

for i in range(21):
    if i %2 ==0:
        print(i)

# Sum of list

numbers1 = [5,15,25,35,45]
t = 0
for n in numbers1:
    t = t + n
print(f"total: {t}")

# Multiplication Table
number = int(input("Enter the number: "))
for table in range(1, 11):
    tab = number * table
    print(f"Table {tab}")

# Count Down

for cout in range(10,0,-1):
    print(f"Count: {cout}")


numbers3 = [1,3,3,4,5]
for  num3 in numbers3:
    num3=num3 **2
    print(f"Sqr {num3}")

# FizzBuzz

for f in range(1,31):
    if f % 3 ==0 and f % 5 == 0:
        print("FizzBuzz")
    elif f % 3 == 0:
        print("Fizz")
    elif f % 5 ==0:
        print("Buzz")
    else:
        print(f)


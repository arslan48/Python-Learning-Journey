numbers = [12, 7, 15, 22, 30, 41, 55, 60]
odd_num = 0
even_num = 0

for i in numbers:
    if i %2 == 0:
        print(f"{i} is even number")
        even_num += 1
        
    else:
        print(f"{i} is odd number")
        odd_num += 1
        
print(f"Total even numbers in this list {even_num}")
print(f"Total odd numbers in this list {odd_num}")

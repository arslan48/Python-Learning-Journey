def even_odd(numbers):
    even_num = []
    odd_num = []
    for num in numbers:
        if num % 2 == 0:
            even_num.append(num)
        else: 
            odd_num.append(num)
    print(f"Even numbers {even_num}")
    print(f"Odd numbers {odd_num} ")
my_list = [334,54,52,57,1,0,5,7,9]
even_odd(my_list)
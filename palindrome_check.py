mixed_list = [3, "abc", "abc", 1]
numbers = [1, 2, 3, 2, 1]

reversed_mixed_list = mixed_list.copy()
reversed_mixed_list.reverse()

reversed_numbers = numbers.copy()
reversed_numbers.reverse()

if reversed_mixed_list == mixed_list:
    print("palindrome")
elif reversed_numbers == numbers:
    print("palindrome numbers")
else:
    print("not a palindrome")
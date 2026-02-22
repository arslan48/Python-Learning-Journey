expenses = [ 1200, 450, 3000, 800, 150, 2200, 600]
total_sum = 0
expensive_item_count = 0

for i in expenses:
    total_sum += i
    if i > 1000:

        print(f" Expensive Expense: {i}")
        expensive_item_count += 1
    else:
        pass

print(f" Total  {int(total_sum)}")
print(f"Expensive items: {expensive_item_count}")

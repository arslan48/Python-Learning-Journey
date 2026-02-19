mixed_data = ["Apple", 50, "Banana", 120, "Cherry", 80, 20]
price_only = []
for data in mixed_data:
    if type(data) == int:
        price_only.append(data)
    else:
       type(data) == str
print(price_only)
print(sum(price_only))

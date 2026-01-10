order_info = "Customer:Zain_Item:Laptop_Price:50000_Status:Paid"
parts = order_info.split("_")
sparts = order_info.split(":")
status = sparts[-1]
reverse_price = sparts[-2][::-1]
print(status)
print(reverse_price)
# Dictionary representing the warehouse data
warehouse = {
    "electronics": {
        "laptop": 50000,
        "phone": 30000
    },
    # Using a set for stock_ids to ensure uniqueness
    "stock_ids": {
        101, 102, 103
    },
    "settings": {
        "tax_rate": 15,  # Tax rate in percentage
        "main_points": 100
    }
}

# --- Operations ---

# Adding a new product to electronics
warehouse["electronics"]["tablet"] = 1500

# Adding a new stock ID
warehouse["stock_ids"].add(104)

# --- Price Calculation ---

# Get the price of the laptop
laptop_price = warehouse["electronics"]["laptop"]

# Apply discount based on price
if laptop_price > 40000:
    print("Price is high (above 40,000). Applying 10% discount.")
    # 10% discount
    price_after_discount = laptop_price * 0.90
else:
    print("Price is reasonable. Applying 5% discount.")
    # 5% discount
    price_after_discount = laptop_price * 0.95

print(f"Price after discount: {price_after_discount}")
print(f"add 15% tax {price_after_discount * 1.15}")






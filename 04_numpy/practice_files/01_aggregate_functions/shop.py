import numpy as np

sales = np.array([[500, 300, 700, 200],
                  [400, 600, 100, 800],
                  [900, 150, 450, 350]])

total_sales = np.sum(sales)
average_per_shop = np.mean(sales, axis=1)
max_per_product = np.max(sales, axis=0)
min_sale = np.min(sales)
std_dev = np.std(sales,axis=1)

print(f"Total sales: {total_sales}")
print(f"Average sales per shop: {average_per_shop}")
print(f"Max sales per product: {max_per_product}")
print(f"Minimum sale: {min_sale}")
print(f"Standard deviation: {std_dev}")
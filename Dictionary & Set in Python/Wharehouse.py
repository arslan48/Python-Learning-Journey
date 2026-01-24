warehouse = {
    "section_a": {"item": "Laptop", "stock": 10, "price": 50000},
    "section_b": {"item": "Mouse", "stock": 50, "price": 1000}
}

print(warehouse.get("section_c", "Section is not active"))
print(warehouse)

warehouse["section_a"]["stock"] = 15
print(warehouse)

Restock = warehouse.update({"section_c": {"item": "keyboard", "stock": 20, "price": 500}})
print(Restock)

soldout = warehouse.pop("section_b")
print("Mouse has been cleared.", soldout)
print(warehouse)
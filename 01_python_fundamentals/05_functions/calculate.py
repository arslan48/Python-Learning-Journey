def calculator(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b

print(calculator(10, 5))
print(calculator(10, 5, "sub"))
print(calculator(10, 5, "mul"))
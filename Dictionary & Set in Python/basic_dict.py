student = {
    "name": "Alice",
    "age": 32,
    "city": "Tokyo"
}

del student["city"]
student["age"] = 55
print(student["age"])
print(student.items())


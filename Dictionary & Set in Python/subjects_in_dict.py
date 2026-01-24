marks ={}
x = int(input("Enter chemistry marks: "))
marks.update({"chemistry": x})
y = int(input("Enter the physics marks:"))
marks.update({"Physics": y})
z = int(input("Enter the Maths marks:"))
marks.update({"Maths": z})
print(marks.items())
print(f"He scrooed {marks}")
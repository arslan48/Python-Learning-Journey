contacts = {}
for i in range(3):
    name = input("Enter the name: ")
    contact = (input("Enter contact number:"))
    contacts[name] = contact
with open("contacts.txt", "a") as f:
    for name, contact in contacts.items(): 
        f.write(f"Name: {name} | Contact: {contact}\n")
print("Info saved")



    
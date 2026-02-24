guests = ["VIP_Ali", "Zain", "VIP_Sara", "Hamza", "VIP_Dua"]
dictionary = {}
for name in guests:
    if name[0:4] == "VIP_":

        realname = name[4:]
        dictionary[realname]= "confirmed"  
print(dictionary) 
vip_guests = ["Ali", "Asim", "Hamza", "Zain"]

people_at_gate = ["Asim", "Bilal", "Zain", "Sara", "Ali"]

for check in people_at_gate:
    if (check in vip_guests):
        print(f"WElCOME {check} You are a VIP")
    else:
        print(f"Sorry {check}, you are not on the list.")
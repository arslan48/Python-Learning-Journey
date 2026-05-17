guest = ['Ali', 'Zain', 'Sara', 'Hamza', 'Dua']
for i in range(len(guest)):
    if i == 0 or i ==4:
        print(f"set {i}: {guest[i]} (VIP)")
    else:
        print(f"{i} {guest[i]}")
    
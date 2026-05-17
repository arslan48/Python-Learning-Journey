morning_staff = {"Zain", "Ali", "Sara", "Ahmed", "Khan"}
evening_staff = {"Sara", "Ahmed", "Hamza", "Zoha", "Bilal"}

morning_staff.add("Raza")
morning_staff.add("Zain")
print(morning_staff)

double_shift = morning_staff.intersection((evening_staff))
print(double_shift)

The_whole_team = morning_staff.union((evening_staff))
print("The whole team is:",The_whole_team)
morning_staff.discard("Zain")
print(f"After Zain left {morning_staff}")

tornament = {"title":"iron first 2026", "prize":50000}

reg = ["Ali", "Zain", "Sara", "Khan", "Khan", "Sara"]
players =set(reg)

new_entery = players.add("Fakhar")
Discolified = players.discard("Khan")
Total_people = len(players)
remaining_prize = tornament['prize'] * 0.9
Entery_fee = 1000
tax = 5

print(f"Tournament name:{tornament['title'].title()}\n Total players:{Total_people}\n Total collection:{(Entery_fee*Total_people)* 1.05}\n Remaining prize pool after admin fee:{remaining_prize}")
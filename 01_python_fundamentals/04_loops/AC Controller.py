ac_on = False
while ac_on == False:
    temp = int(input("What is Temprature: "))
    is_some_one_room = input("Is anybody in room: ")
    manual = input("Can we on a ac forcefylly: ")
    if temp > 30 and (is_some_one_room == "yes" or manual == "yes"):
        print(f"Ac is turned on and room temprature is: {temp} now ")
        break
    else:
        print("Ac is off")
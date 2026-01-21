Supported_countries = ("Austrila", "Germany", "Canada", "Turkey", "Japan")
user_input = input("Which country do you want to apply: "). title()
if user_input in Supported_countries:
    print("Success! We can help you with your visa for " + user_input)
else:
    print("Sorry, we don't support that country yet.")
    
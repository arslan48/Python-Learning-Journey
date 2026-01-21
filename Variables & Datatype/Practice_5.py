# This is a ticket booking program using if elif else conditions and using And and Or operators and usung in operator
City_name = input("Enter a city name: ").lower()
Ticket_type = input("Enter a ticket type (regular/vip/guest): ").lower()
Day = input("Enter a day weekday/weekend: ").lower()
Allowed_cities_list = ["karachi", "lahore", "islamabad"]
Allowed_tickets_types = ["regular", "vip", "guest"]
if City_name in Allowed_cities_list and Ticket_type in Allowed_tickets_types and Day == "weekend":
    print("Ticket allowed")
elif City_name in Allowed_cities_list and Ticket_type in Allowed_tickets_types and Day == "weekday":
    print("Ticket allowed")    
else:
    print("Ticket not allowed") 

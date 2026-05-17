# Registration Data
event_info = {"name": "python summit 2026", "location": "islamabad"}

# Participants 
participants_list = ["ali", "sara", "ali", "zain", "sara", "ahmed"]

# Fees
ticket_price = 1000
tax = 150


Unique_participants =set(participants_list)
Unique_participants.add("Hamza")
total_people = len(Unique_participants)

total_bill = total_people*(ticket_price+tax)

print(f"Event name: {event_info['name'].title()}\n Location name: {event_info['location'].upper()}\n Total people: {total_people}\n total bill: {total_bill}")
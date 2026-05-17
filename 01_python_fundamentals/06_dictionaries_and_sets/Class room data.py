school = {
    "student":{

        "name":"ali", 
        "fee":2000

     },
    "status":{

        "is_paid": False, 
      "discount": 10
    }

}    
final_fee =school["student"]["fee"]*0.90
school['status']['is_paid'] = True

print(f"the student name is: {school['student']['name'].title()}")
print(f"fee after discount: {final_fee}")
print(f"Updated Status: {school['status']['is_paid']}")

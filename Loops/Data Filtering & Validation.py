party_list = [] 

while True:
    name = input("Enter friend's name (or type 'done' to finish): ")
    
    if name == "done": 
        break
        
    if len(name) < 3:
        print("Name is too short!") 
        continue
    
    
    party_list.append(name)
    print(f"{name} added to list")


print("Final Party List:", party_list)
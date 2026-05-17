num = list(range(1, 21))
i = 0

while i < len(num): 
    current_num = num[i]
    
    if current_num > 15:  
        break
    
    if current_num % 3 == 0:  
        print(current_num)
    
    i += 1  
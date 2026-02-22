passwords = ["123", "python321", "abc", "secure786", "pwr", "admin123"]
strong_count = 0
for i in passwords:
    if len(i) >= 6:
        print(f"{i} Strong password")
        strong_count += 1
        
    else:
        print(f"{i} Weak passwords ")
        
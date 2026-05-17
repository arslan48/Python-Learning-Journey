passwords =['12345', 'password', 'admin', 'qwerty', '112233']
for i in passwords:
    if  len(i) < 6 :
        print(f"Unsafe {i}")
    else:
        print(f"Safe  {i}")


for i in range(3):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    
   
    if marks >= 50:
        status = "PASS"
    else:
        status = "FAIL"
    

    with open("result.txt", "a") as f:
        f.write(f"Student: {name}, Marks: {marks}, Result: {status}\n")

print("--- All students data saved on result.txt file! ---")
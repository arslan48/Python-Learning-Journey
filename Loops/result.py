grades = ["A", "B", "F", "A", "C", "F", "B", "A"]
pass_count = 0 
fail_count = 0
for check in grades:
    if check == "F":
        fail_count += 1
    else:
        pass_count +=1
print(f"Total passed {pass_count}")
print(f"Total failed {fail_count} ")
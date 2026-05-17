marks_list = [45, 78, 32, 90, 55, 28, 85]
fail_count = 0
for marks in marks_list:
    if marks >= 33:
        print(f"You pass and you contain {marks} marks")
    else:
        print("Fail")
        fail_count += 1
print(f"Fail students are {fail_count}")
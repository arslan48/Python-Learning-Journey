attendence =['P', 'A', 'P', 'P', 'A', 'P', 'A', 'P']
absent_student = 0
present_student = 0
for absents in attendence:
    if absents == "A":
        absent_student += 1
    else:
        present_student += 1
print(f"The absent students are: {absent_student}")

absent_count = 0
present_count = 0
for i in range(1, 31):
    ask = input(f"Day {i}: Was the student present? (P/A): ").upper()
    if ask == "A":
        absent_count += 1
    else:
        present_count += 1
print(f"Absent students {absent_count}")
        
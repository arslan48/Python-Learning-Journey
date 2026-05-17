marks_book = {"Ali": 85, "Sara": 40, "Zain": 75, "Dua": 30}
for name, marks in marks_book.items():
    if marks >= 40:
        print(f"{name} - Congratulations! You passed with {marks} marks.")
    else:
        print(f"{name} - Sorry! you failed {marks}")
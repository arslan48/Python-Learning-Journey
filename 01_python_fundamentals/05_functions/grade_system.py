def grade_system():
    for i in range(5):
        name = input("Enter your name: ")
        marks = int(input("Enter your marks: "))
        if  marks >= 95:
            print(f"Congratulations you got A grade {name}")
        elif marks >= 80:
            print(f"{name} Grade B")
        elif marks >= 70:
            print(f"{name} Grade C")
        elif marks >= 40:
            print(f"{name} Grade D")
        else:
            print(f"{name} Grade F")

grade_system()


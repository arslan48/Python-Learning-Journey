def grade_check(score):
    if score > 50:
        return "Congradulation you have passed the exam"
    else:
        return "sorry try again"
marks = int(input("Enter the marks: "))
result = grade_check(marks)
print(result)
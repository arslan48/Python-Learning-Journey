Age = int (input("Enter your age: "))
IELTS_Score = float (input("Enter your IELTS score: "))
Acceptance_letter = input("Do you have and Acceptance letter from a university yes/no: ")
if 17 < Age < 35 and IELTS_Score >= 6.0 :
    print("You are eligible for a student visa")
elif  17 < Age < 35 and (IELTS_Score < 6.0  or Acceptance_letter == "yes"):
        print("You are still eligible ")
else:
     print("You are not eligible for a student visa")
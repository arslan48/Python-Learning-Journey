# This is a job application program using if elif else conditions and using And and Or operators
Age = int(input("Enter your age: "))
Education = input("Enter your education level (matric/intermediate/bachelor): ").lower()
Experience = int(input("Enter your experience in years: "))
English_proficiency = input("Do you have English proficiency (yes/no): ").lower()

valid_education_levels = ["matric", "intermediate", "bachelor"]

if Age >= 18 and Education in valid_education_levels and Experience >= 2 and English_proficiency == "yes":
    print("Selected")

elif Age >= 18 or Education in valid_education_levels or Experience >= 2 or English_proficiency == "yes":
    print("Interview Allowed")

else:
    print("Rejected")

company = {
    "emp1": {
        "name": "Zain",
        "role": "Python Developer",
        },
    "emp2": {
        "name": "Ali",
        "role": "Designer",
        }
}
print(f"The role of Ali is {company['emp2']['role']}")

New_employee = {
    "name": "Khan",
    "role": "manager"

}

company.update({"emp3": New_employee})
company["emp1"]["role"] = "Senior Python Developer"
print(company)

Add_list =company["emp1"]["skills"] = ["Python", "Django", "Git"]
print(company)
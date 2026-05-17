about ={
    "name":"Zain",
    "age": 21,
    "Subjects": {
        "Maths": 90,
        "Science": 85,
        "English": 88
    } 
}
print(about)
print(about["Subjects"])
order = about.items()
print(order)

print(f"My name is {about['name']} and i am {about['age']} years old .  and my faveriote subjects are {about['Subjects'].keys()} " )
user_profile = ("Ali_Khan", 19, "Lahore", "Editor")
tem_profile = list(user_profile)
tem_profile[1] = 21
tem_profile[2] = "Islamabad"
tem_profile.append("verified")
user_profile = tuple(tem_profile)
name,age,city,profession,status = user_profile
print(f"{name} is {age} years old {profession} and lives in {city}")
print(status)
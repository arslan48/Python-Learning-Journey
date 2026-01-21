user_profile = {
    "username": "Zain34",
    "email": "zain34@gmail.com",
    "status": "Active"
}
user_profile.pop("email")
print(user_profile)
print("status" in user_profile)
print(len(user_profile))
print(user_profile.keys())
print(user_profile.values())
print(user_profile.items())
user_profile = {
    "username": "Zain33",
    "followers": "500",
}

user_profile.update({"followers": "558"})
main=user_profile.items()
print(main)

The_safe_serch = user_profile.get("location", "Location not set")
print(The_safe_serch)

print(user_profile.keys())
print(user_profile.values())

deleted_user =user_profile.pop("username")
print(deleted_user)

user_profile.clear()
print(user_profile)
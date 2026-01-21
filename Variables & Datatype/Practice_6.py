# Access Control Logic: Determines user permissions based on subscription, age, and content category.
# Concepts used: Variables, Lists, Logical operators (and), Membership operators (in), and Nested conditionals.
User_subscription_plan = "premium"
User_age = 18
content_category = "all"
Allowed_categories_list = ["all", "movies", "series", "anime"]
if User_subscription_plan == "premium" and content_category in Allowed_categories_list:
    if User_age >= 18:
        print("Full access allowed")
    else:
        print("Partial access allowed")
else:
    print("Access not allowed")



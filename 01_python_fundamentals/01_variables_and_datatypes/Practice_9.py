user_age = 17
subscription = "standard"
country = "pakistan"
course_type = "advanced"
payment_status = "paid"

allowed_countries = ["pakistan", "india", "uk"]

if (user_age >= 18 and 
    subscription == "premium" and 
    payment_status == "paid" and 
    country in allowed_countries):
    print("Full access granted")

elif ((subscription == "standard" or subscription == "premium") and 
      payment_status == "paid" and 
      course_type == "basic" and 
      country in allowed_countries):
    print("Limited access granted")

else:
    print("Access denied")
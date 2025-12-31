# Prompt user to enter their age and convert it to an integer
age = int(input("Enter age: "))

# Prompt user to enter their subscription plan and convert to lowercase for consistency
subscription = input("Enter plan (free/premium): ").lower()

# Prompt user to enter their device type and convert to lowercase
device = input("Enter device (mobile/laptop): ").lower()

# Define a list of allowed devices
allowed_devices = ["mobile", "laptop"]

# Check for full access: User must be 18 or older, have premium, and use an allowed device
if age >= 18 and subscription == "premium" and device in allowed_devices:
    print("Full access granted")

# Check for limited access: User is under 18, has premium, but is restricted to mobile only
elif age < 18 and (subscription == "premium") and device == "mobile":
    print("Limited access granted")

# If neither condition is met, access is denied
else:
    print("Access denied")

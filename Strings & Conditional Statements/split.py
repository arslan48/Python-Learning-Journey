email = "john.doe@gmail.com"

Split = email.split("@") 
username = Split[0]
domain = Split[1]

Extract_gmail = domain.split(".")[0]

print("Username:", username)
print("Website:", Extract_gmail)

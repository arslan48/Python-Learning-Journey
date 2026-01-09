# The secret message
data = "!!!321_ma_i_trapxE_nohtyP_olleh!!!"

# Print how many characters are in the string
print(len(data ))

# Remove the first 3 "!!!" and the last 3 "!!!"
Clear_data = data[3:-3]

# Extract the part "trapxE_nohtyP" from the middle
Secret_World = Clear_data[9:22]

# Reverse it to get "Python_Expert"
secret_world = Secret_World[::-1]

# Extract the numbers "321" from the beginning
number = Clear_data[:3]

# Reverse the numbers to get "123"
reverse_number = number[::-1]

# Join the numbers and the text
Magic_World = reverse_number + secret_world

# Print the final result: "123Python_Expert"
print(Magic_World)

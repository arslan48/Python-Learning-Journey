sentence = "apple is a orange"

vowels = "aeiou"
count = 0

for word in sentence.split():
    if word[0].lower() in vowels:
        count += 1

print(count)
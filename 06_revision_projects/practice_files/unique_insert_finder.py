friend = {
    "Ali": ["farming", "gaming", "reading"],
    "Sara": ["cooking", "reading", "gardening"],
    "Ahmed": ["gaming", "gardening"],
    "Shid": ["stamp collecting", "coin collection"]
}

hobbies = set()

for hobbies_list in friend.values():
    hobbies.update(hobbies_list)
print(f"Unique hobbies of my friends are: {hobbies}")

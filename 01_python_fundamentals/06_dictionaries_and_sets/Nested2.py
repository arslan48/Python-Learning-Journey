library = {
    "book1": {"title": "Python Basics", "copies": 5},
    "book2": {"title": "Web Design", "copies": 3}
}

check = library.get("book3", "Not Found")
print(check)

library["book1"]["copies"] = 10

library["book3"] = {"title": "Data Science", "copies": 2}

print(library["book2"]["title"])    
remove = library.pop("book2")
print(remove)
print(library["book1"]["title"])

user_settings = {"theme": "Dark", "font_size": 16}
language = input("Enter the language: ")
check = user_settings.get(language, "English")
print(check)
theam = user_settings.get("theme", "Dark")
print(theam)
raw_names = ["  ali ", "SARA", "  zaIn ", " hAmZa  ", "DUA"]
clean_names = []

for name in raw_names:
    
    clean = name.strip().capitalize()
    clean_names.append(clean)

print(f"Raw names are {raw_names}")
print(f"Clean names are {clean_names}")
raw_data = "REDACTED_ali_khan_2004_ERROR"
remove = raw_data[9:-6]
extract_name = remove[:8]
extract_year = remove[-4:]
reverse = extract_year[::-1]
nick_name = extract_name[:3] +extract_year[-2:]
print("Name",extract_name)
print("Year",extract_year)
print("Reverse",reverse)
print("Nick Name",nick_name)
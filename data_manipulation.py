raw_data = [500, 10, 200, 5, 20, 100, 30, 450]
raw_data.remove(500)
raw_data.remove(450)
raw_data.sort()
raw_data.insert(3,99)
removed_item = raw_data.pop(6)
print(raw_data)

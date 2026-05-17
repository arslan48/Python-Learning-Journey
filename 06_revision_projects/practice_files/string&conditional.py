data = "  ML-Model-2026_Final  "
remove = data.strip()
if len(remove) > 10 and "2026" in remove:
    print("Valid Data for ML")
else:
    print("Invalid data")
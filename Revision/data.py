accuracies = [0.95, 0.70, 0.45, 0.88, 0.30]
for score in accuracies:
    if score > 0.85:
        print(f"Excellent Model: your accuracies is: {score}")
    elif score > 0.50:
        print(f"Good Model your accuracies is: {score}")
    else:
        pass
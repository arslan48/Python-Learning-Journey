import numpy as np

prices = np.array([150, 320, 85, 450, 200])
quantities = np.array([2, 1, 5, 1, 3])

def calculate_bill(price,quantities):
    print(f"--Shop Bill--")

    total = price * quantities
    grand_total = np.sum(total)
    expensive = np.max(total)
    cheapest = np.min(total)
    average = np.mean(total)
    print(f"Item totals: {total}")
    print(f"Grand Total: {grand_total}")
    print(f"Expensive:   {expensive}")
    print(f"Cheapest:    {cheapest}")
    print(f"Average:     {average}")

calculate_bill(prices, quantities)
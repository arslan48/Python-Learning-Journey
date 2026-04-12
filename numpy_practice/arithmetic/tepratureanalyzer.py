import numpy as np

week1 = np.array([32, 35, 30, 38, 33, 29, 36])
week2 = np.array([28, 31, 33, 35, 30, 27, 29])

def analyze_temp(temps, week_name):
    print(f"--{week_name}---")
    average = np.mean(temps)
    hottest = np.max(temps)
    coldest = np.min(temps)
    median = np.median(temps)
    above32 = len(temps[temps> 32])

    print(f"Average:  {average:.2f}")
    print(f"Hottest:  {hottest}")
    print(f"Coldest:  {coldest}")
    print(f"Median:   {median}")
    print(f"Above 32: {above32} days")

analyze_temp(week1, "week1")

analyze_temp(week2, "week2")

if np.mean(week1) > np.mean(week2):
    print("Week1 is hotter")
else:
    print("week2 is hotter")
    

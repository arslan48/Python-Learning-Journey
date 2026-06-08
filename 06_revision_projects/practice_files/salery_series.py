from matplotlib.pylab import ma
import pandas as pd 

df = pd.read_csv("employees.csv")
s = df["Salary"]
print(s)
avg_salary = s.mean()
print("\nAverage Salary\n")
print("\naverage Salary")
print(avg_salary)

high_earners = df[s > 90000]["Name"]
print("\nHigh Earners")
print(high_earners)

max_sal = s.max()
highest_salary = df[s==max_sal][["Name","Salary"]]
outlier = df[s>1000000]["Name"]
print("\nOutlier\n")
print(outlier)
print("\nHighest_salary\n")
print(highest_salary)
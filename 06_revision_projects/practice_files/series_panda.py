import pandas as pd 

cities_population = {
    "New York":8336817,
    "Los Angeles":3979576,
    "Chicago":2693976,
    "Houston": 2304580,
    "Phoenix": 1608139
}

series = pd.Series(cities_population)
print(series)

print("\nChicago population\n")
print(series.loc["Chicago"])

print("\nFirst city population\n")
print(series.iloc[0])

large_cities=series[series >= 2000000 ]
print("\nLarge cities\n")
print(large_cities)
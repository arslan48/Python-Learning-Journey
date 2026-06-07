import pandas as pd

cities = {
    "Dubai": 42,
    "London": 18,
    "Tokyo": 31,
    "New York": 28,
    "Sydney": 22
}

movies = {
    "Inception": 8.8,
    "Interstellar": 8.7,
    "The Dark Knight": 9.0,
    "Oppenheimer": 8.9,
    "Dune Part Two": 8.5
}

series = pd.Series(cities)
print(series)

max_tem = series[series > 30] 
print(max_tem)

tokyo_temp = series.loc["Tokyo"]
print(f"Temprature of Tokyo is {tokyo_temp}")

mov_s = pd.Series(movies)
print(mov_s)

highter_rating_movies = mov_s[mov_s > 8.8]
print("\nHigh rating movies\n")
print(highter_rating_movies)

lowest_rating = mov_s.min()
print("\nLowest rating movies")
print(mov_s[mov_s ==lowest_rating])

print("\nThird movie rating\n")
print(mov_s.iloc[2])

user_account = {
 "profile":{
    "name": "Hassan",
    "balance": 5000,
    "plan": {
        "name": "premium",
        "cost": 3000,
        "watched_movies": {"Matrix", "Titanic"}
    }
 }   
}
New_movie = "Avatar"
user_account["profile"]["plan"]["watched_movies"].add(New_movie)

dublicate_movie = "Matrix"
user_account["profile"]["plan"]["watched_movies"].add(dublicate_movie)
print(f"The movies watched by {user_account['profile']['name']} are: {user_account['profile']['plan']['watched_movies']}")

    
gaming_cafe = {
    "customer": {
        "name": "Zain",
        "points": 150
    },
    "session": {
        "hours": 3,
        "rate_per_hour": 500
    },
    "games_played": {"GTA", "FIFA", "Tekken"}
}


gaming_cafe["games_played"].add("Valorant")



gaming_cafe["customer"]["points"] = 150



total_bill = gaming_cafe["session"]["hours"] * gaming_cafe["session"]["rate_per_hour"]
after_tax = total_bill * 1.15  
final_bill = after_tax * 0.90 
# 4. Result
print(f"Customer: {gaming_cafe['customer']['name']}")
print(f"Total Games Played: {len(gaming_cafe['games_played'])}")
print(f"Final Bill to Pay: {final_bill}")
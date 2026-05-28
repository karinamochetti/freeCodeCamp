def get_hill_rating(drop, distance, hill_type):
    steepness = drop/distance
    multiply = {
        "Downhill": 1.2,
        "Slalom": 0.9,
        "Giant Slalom": 1.0,
    }
    steepness *= multiply[hill_type]

    if steepness <= 0.1: return "Green"
    elif steepness <= 0.25: return "Blue"
    else: return "Black"

print(get_hill_rating(95, 900, "Slalom"))
print(get_hill_rating(620, 2800, "Downhill"))
print(get_hill_rating(420, 1680, "Giant Slalom") )
print(get_hill_rating(250, 3000, "Downhill"))
print(get_hill_rating(110, 900, "Slalom"))
print(get_hill_rating(380, 1500, "Giant Slalom"))

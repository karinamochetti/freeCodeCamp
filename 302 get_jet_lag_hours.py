def get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction):
    TIMEZONE = {
        "Los Angeles": -8,
        "New York": -5,
        "London": 0,
        "Istanbul": +3,
        "Dubai": +4,
        "Hong Kong": +8,
        "Tokyo": +9,
    }
    timezone_diff = TIMEZONE[arrival_city]-TIMEZONE[departure_city] if TIMEZONE[arrival_city] > TIMEZONE[departure_city] else TIMEZONE[departure_city]-TIMEZONE[arrival_city]
    multiplier = 1.5 if direction == "east" else 1.0
    return timezone_diff + (flight_duration * 0.1) *  multiplier

print(get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east"))
print(get_jet_lag_hours("London", "New York", 8, "west"))
print(get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east"))
print(get_jet_lag_hours("Dubai", "London", 7, "west"))
print(get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west"))
print(get_jet_lag_hours("Tokyo", "Dubai", 9, "west"))
print(get_jet_lag_hours("New York", "Istanbul", 10, "east"))

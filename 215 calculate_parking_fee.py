def calculate_parking_fee(park_time, pickup_time):
    print()
    park_min = int(park_time[0:2])*60 + int(park_time[3:])
    pickup_min = int(pickup_time[0:2])*60 + int(pickup_time[3:])

    cost = 0

    minutes_parked = pickup_min-park_min
    if minutes_parked < 0:
        cost += 10
        minutes_parked = 1440 + minutes_parked

    cost += (minutes_parked//60)*3

    if minutes_parked%60 > 0:
        cost += 3

    cost = max(5, cost)

    return f"${cost}"

print(calculate_parking_fee("09:00", "11:00"))
print(calculate_parking_fee("10:00", "10:30"))
print(calculate_parking_fee("08:10", "10:45"))
print(calculate_parking_fee("14:40", "23:10"))
print(calculate_parking_fee("18:15", "01:30"))
print(calculate_parking_fee("11:11", "11:10"))
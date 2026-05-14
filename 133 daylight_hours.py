def daylight_hours(latitude):
    table = {
        -90: 24,
        -75: 23,
        -60: 21,
        -45: 15,
        -30: 13,
        -15: 12,
        0: 12,
        15: 11,
        30: 10,
        45: 9,
        60: 6,
        75: 2,
        90: 0,
    }
    if latitude%15 <= 7:
        return table[(latitude//15)*15]
    else:
        return table[((latitude//15) + 1)*15]

print(daylight_hours(45))
print(daylight_hours(0))
print(daylight_hours(-90))
print(daylight_hours(-10))
print(daylight_hours(23))
print(daylight_hours(88))
print(daylight_hours(-33))
print(daylight_hours(70))

def get_daytime_hours(latitude):
    raw_sun = 12 + (latitude / 90) * 12
    sun = int(2 * round(raw_sun / 2))
    moon_half = (24 - sun) // 2
    return "🌑"*moon_half + "☀️"*sun + "🌑"*moon_half

print(get_daytime_hours(0))
print(get_daytime_hours(90))
print(get_daytime_hours(-90))
print(get_daytime_hours(-33))
print(get_daytime_hours(66.5))
print(get_daytime_hours(40))
print(get_daytime_hours(-50))

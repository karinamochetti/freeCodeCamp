def get_spoken_time(hour_angle, minute_angle):
    h = hour_angle*12//360
    m = minute_angle*60//360
    if m == 0:
        return f"{h:.0f} o'clock"
    if m == 15:
        return f"quarter past {h:.0f}"
    if m == 30:
        return f"half past {h:.0f}"
    if m == 45:
        return f"quarter to {h+1:.0f}"
    if 1 <= m <= 29:
        return f"{m} minutes past {h:.0f}"
    if 31 <= m <= 59:
        return f"{60-m} minutes to {h+1:.0f}"
    return minute_angle*60//360


print(get_spoken_time(90, 0))
print(get_spoken_time(160, 120))
print(get_spoken_time(255, 180))
print(get_spoken_time(67.5, 92))
print(get_spoken_time(200, 240))
print(get_spoken_time(322.5, 273))
print(get_spoken_time(117.5, 335))

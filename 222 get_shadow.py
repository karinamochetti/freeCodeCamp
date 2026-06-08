def get_shadow(time):
    h_str, m_str = time.split(":")
    hour = int(h_str) + int(m_str) / 60
    if hour < 6 or hour >= 18 or hour == 12:
        return "No shadow"
    length = abs(12 - hour) ** 3
    direction = "west" if hour < 12 else "east"
    return f"{length:g}ft {direction}"

print(get_shadow("10:00"))
print(get_shadow("15:00"))
print(get_shadow("12:00"))
print(get_shadow("17:30"))
print(get_shadow("05:00"))
print(get_shadow("06:00"))
print(get_shadow("18:00"))
print(get_shadow("07:30"))
print(get_shadow("00:00"))


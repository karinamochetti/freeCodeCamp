def get_greeting(s):
    hour, minute = s.split(":")
    if 5 <= int(hour) < 12: return "Good morning"
    elif 12 <= int(hour) < 18: return "Good afternoon"
    elif 18 <= int(hour) < 22: return "Good evening"
    else: return "Good night"

print(get_greeting("06:30"))
print(get_greeting("12:00"))
print(get_greeting("21:59"))
print(get_greeting("00:01"))
print(get_greeting("11:30"))

def mile_pace(miles, duration):
    duration = duration.split(":")
    seconds = 60*int(duration[0]) + int(duration[1])
    speed = seconds / miles
    s = int(speed%60)
    m = int(speed//60)
    return f"{m:02}:{s:02}"


print(mile_pace(3, "24:00"))
print(mile_pace(1, "06:45"))
print(mile_pace(2, "07:00"))
print(mile_pace(26.2, "120:35"))

def get_direction(time1, time2):
    h1, m1 = map(int, time1.split(":"))
    h2, m2 = map(int, time2.split(":"))
    
    minutes_in_day = 24 * 60
    half_day = minutes_in_day // 2

    diff = ((h2 * 60 + m2) - (h1 * 60 + m1)) % minutes_in_day

    if diff == 0 or diff == half_day:
        return "equal"
    if diff < half_day:
        return "forward"  
    else:
        return "backward"



print(get_direction("10:00", "12:00"))
print(get_direction("11:00", "05:00"))
print(get_direction("00:00", "12:00"))
print(get_direction("15:45", "01:10") )
print(get_direction("03:30", "19:50"))
print(get_direction("06:30", "18:30"))
